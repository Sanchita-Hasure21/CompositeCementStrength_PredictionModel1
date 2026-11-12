# Step3: Model Training and Evaluation
from sklearn.linear_model import LinearRegression,Ridge,Lasso,HuberRegressor,RANSACRegressor,TheilSenRegressor,ElasticNet,SGDRegressor
from sklearn.metrics import r2_score

scores =[]

def model_build(X_train,X_test,y_train,y_test):
  models = {'LinearRegression':LinearRegression(),
      'Ridge':Ridge(),
      'Lasso':Lasso(),
      'HuberRegressor':HuberRegressor(),
      'RANSACRegressor':RANSACRegressor(),
      'TheilSenRegressor':TheilSenRegressor(),
      'ElasticNet':ElasticNet(),
      'SGDRegressor':SGDRegressor()
      }

  for model_name,model in models.items():
    model.fit(X_train,y_train) #seen data
    y_pred = model.predict(X_test) #Unseen data
    r2 = r2_score(y_test,y_pred) #r2score = (1 - error)
    scores.append(r2)
    print(f'{model_name} R2 score: {r2}')
  return scores