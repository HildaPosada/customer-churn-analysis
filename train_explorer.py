"""Build a held-out churn explorer from the committed Telco dataset."""
from pathlib import Path
import json
import pandas as pd,numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,accuracy_score
root=Path(__file__).resolve().parent
df=pd.read_csv(root/'data/Telco-Customer-Churn.csv');df['TotalCharges']=pd.to_numeric(df.TotalCharges,errors='coerce')
y=df.Churn.eq('Yes').astype(int);X=df.drop(columns=['Churn','customerID']);a,b=train_test_split(np.arange(len(df)),test_size=.2,stratify=y,random_state=42)
num=X.select_dtypes(include='number').columns.tolist();cat=[k for k in X if k not in num]
prep=ColumnTransformer([('numeric',Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]),num),('category',OneHotEncoder(handle_unknown='ignore'),cat)])
model=Pipeline([('prepare',prep),('model',LogisticRegression(max_iter=1500,random_state=42))]);model.fit(X.iloc[a],y.iloc[a]);score=model.predict_proba(X.iloc[b])[:,1]
features=model['prepare'].get_feature_names_out();transformed=model['prepare'].transform(X.iloc[b]);contribution=transformed.multiply(model['model'].coef_) if hasattr(transformed,'multiply') else transformed*model['model'].coef_;contribution=contribution.toarray() if hasattr(contribution,'toarray') else contribution
rows=[]
for i,index in enumerate(b):
 pos=np.argsort(contribution[i])[::-1][:3];drivers=[str(features[j]).split('__',1)[-1] for j in pos if contribution[i,j]>0]
 rows.append({'id':str(df.iloc[index].customerID),'score':round(float(score[i]),6),'churn':int(y.iloc[index]),'contract':str(df.iloc[index].Contract),'tenure':int(df.iloc[index].tenure),'monthly_charges':float(df.iloc[index].MonthlyCharges),'drivers':drivers})
out=root/'web';out.mkdir(exist_ok=True)
report={'source':'Committed public Telco Customer Churn dataset','method':'Logistic regression; stratified 80/20 split; seed 42; preprocessing fitted on training only','train_rows':len(a),'test_rows':len(b),'roc_auc':float(roc_auc_score(y.iloc[b],score)),'accuracy_at_50_percent':float(accuracy_score(y.iloc[b],score>=.5)),'rows':rows}
(out/'risk.json').write_text(json.dumps(report,separators=(',',':')))
print({k:v for k,v in report.items() if k!='rows'})
