import sys
import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split


class HousePricePrediction():
  def __init__(self):
    self.data="data.csv"
    df=pd.read_csv(self.data)
    for i in range(len(df)):
      df['bathrooms'] = df['bathrooms'].apply(math.floor)
    df['month'] =pd.to_datetime(df['date']).dt.month
    df.drop(columns=['date'], inplace=True)
    df=df.drop(['statezip','street','country'], axis=1)
    a=df['city'].unique()
    r={}
    for i in range(len(a)):
      r.update({a[i]:i})
    df['city']=df['city'].map(r)
    X=df.iloc[ : ,1:]
    y=df.iloc[ : , 0]
    self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X,y,test_size=0.2, random_state=42)

    #Manual m and c values using matrix multiplication

    # --- Convert pandas to numpy ---
    X_np = self.X_train.values
    y_np = self.y_train.values.reshape(-1, 1)
    # --- Compute means ---
    X_mean =self.X_train.mean().values
    y_mean = float(self.y_train.mean())
    # --- Center the data ---
    X_centered = X_np - X_mean
    y_centered = y_np.flatten() - y_mean

    # --- SVD decomposition ---
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
    # --- Tolerance for numerical stability ---
    tol = 1e-15 * max(X_centered.shape) * S[0]
    S_inv = np.array([1/s if s > tol else 0 for s in S])
    # --- Pseudo-inverse ---
    X_pinv = Vt.T @ np.diag(S_inv) @ U.T
    # --- Coefficients ---
    self.m = X_pinv @ y_centered
    # --- Intercept ---
    self.c = y_mean - np.dot(X_mean, self.m)
    # --- Optional: zero out tiny noise values ---
    self.m[np.abs(self.m) < 1e-10] = 0

  def training(self):
    Train_predictions=[]
    for i in self.X_train.index:
      a=0
      x=0
      for j in self.X_train.columns:
         a+=self.X_train[j][i]*self.m[x]
         x+=1
    Train_predictions.append(a+self.c)
    np.array(Train_predictions)
    #Mean squared error
    y=0
    s=0
    for i in self.y_train.index:
      s+=(self.y_train[i]-Train_predictions[y])**2
      y+=1
    print(f"Mean_Squared_Error:{s/len(self.y_train)}")
    #root_mean_squared_error
    print(f"Root_Mean_Square_Error:{math.sqrt(s/len(self.y_train))}")
    #r2_score
    numerator=0
    denomenator=0
    y=0
    s=0
    mean_y=self.y_train.mean()
    for i in self.y_train.index:
      numerator+=(self.y_train[i]-Train_predictions[y])**2
      denomenator+=(self.y_train[i]-mean_y)**2
      y+=1
    print(f"Training Accuracy:{1-(numerator/denomenator)}")
  def testing():
    try:
      Test_predictions=[]
      for i in self.X_test.index:
        a=0
        x=0
        for j in self.X_test.columns:
          a+=self.X_test[j][i]*self.m[x]
          x+=1
        Test_predictions.append(a+self.c)

      #Mean squared error
      y=0
      s=0
      for i in self.y_test.index:
        s+=(self.y_test[i]-Test_predictions[y])**2
        y+=1
      print(f"Mean_Squared_Error:{s/len(self.y_test)}")

      #r2_score
      numerator=0
      denomenator=0
      y=0
      s=0
      mean_y=self.y_test.mean()
      for i in self.y_test.index:
        numerator+=(self.y_test[i]-Test_predictions[y])**2
        denomenator+=(self.y_test[i]-mean_y)**2
        y+=1
      print(f"Test Accuracy:{1-(numerator/denomenator)}")
    except Exception as e:
      err_ty,err_ms,err_line =sys.exc_info()
      print(f'Error is due to : {err_ty} from Line No : {err_line.tb_lineno}')

  def predict(self,a):
    p=0
    y=0
    for i in a:
      p+=i*self.m[y]
      y+=1
    return p+self.c
