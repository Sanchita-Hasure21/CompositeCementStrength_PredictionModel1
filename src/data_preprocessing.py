
# Step2: Data Preprocessing and Cleaning
from  sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
from sklearn.model_selection import train_test_split
def data_preprocessing(df):
  '''
  step1: Feature Engineering and Feature selection
  step2: split the dataset into independent columns as dependent columns
  ie. X and y
  step3: split the dataset into seen and unseen (seen data : train data
  & Unseen  data : test data)
  step4: Scaling /Normalization the data (Standard Scaler, MinMax Scaler
  Robust Scalar)
  step5: Return the seen and unseen data
  '''
  #Step1: Feature Engineering 
  #Feature Engineering : Create new feature based on existing feature
  df['Water_to_Cementitious_MaterialsRatio'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)'] + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'] + df['Fly Ash (component 3)(kg in a m^3 mixture)'])


  #Step2: Split the dataset into X and y
  target_col ='Concrete compressive strength(MPa, megapascals) '
  X = df.drop(columns =[target_col])
  y = df[target_col]

  #Step3: Split the dataset into Seen(train data ) and Unseen data (test data)
  X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                  test_size=0.3,
                                                  random_state=1)


  #Step4:Normalization /Scaling Technique
  sc = MinMaxScaler()
  X_train = sc.fit_transform(X_train)  #seen data 
  X_test = sc.transform(X_test)       #unseen data 

  return X_train,X_test,y_train,y_test



