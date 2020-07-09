import numpy as np
import pandas as pd
import pickle
url=('https://raw.githubusercontent.com/codophobia/CricketScorePredictor/master/data/t20.csv')
df1=pd.read_csv(url,index_col=0)
df1.head()
df1.isnull().sum()
del1 = ['batsman','bowler','venue','striker','non-striker']
df1.drop(labels=del1,axis=1,inplace= True)
consistent_teams = ['India', 'Australia', 'England',
                    'Pakistan', 'SouthAfrica', 'WestIndies',
                    'SriLanka', 'Newzealand']
df1 = df1[(df1['bat_team'].isin(consistent_teams)) & (df1['bowl_team'].isin(consistent_teams))]
from datetime import datetime
df1['date'] = df1['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
df1=df1[df1['overs']>=5.0]
onehot=pd.get_dummies(data=df1,columns=['bat_team','bowl_team'])
X_train = onehot.drop(labels='total', axis=1)[onehot['date'].dt.year <= 2016]
X_test = onehot.drop(labels='total', axis=1)[onehot['date'].dt.year >= 2017]

y_train = onehot[onehot['date'].dt.year <= 2016]['total'].values
y_test = onehot[onehot['date'].dt.year >= 2017]['total'].values


X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
filename = 't20-model.pkl'
pickle.dump(regressor, open(filename, 'wb'))