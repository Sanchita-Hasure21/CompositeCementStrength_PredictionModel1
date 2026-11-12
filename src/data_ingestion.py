import pandas as pd 
# Step1: Data Ingestion

def data_ingestion():
  '''
  * Title :Composite Cement Strength Prediction Model

  * Shape of the Dataset : (1030,10)

  * Dataset :Concrete_Data.csv

  * Independent Columns :['Cement (component 1)(kg in a m^3 mixture)',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
       'Fly Ash (component 3)(kg in a m^3 mixture)',
       'Water  (component 4)(kg in a m^3 mixture)',
       'Superplasticizer (component 5)(kg in a m^3 mixture)',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)', 'Age (day)',
       'Water_to_Cementitious_MaterialsRatio']

  * Target Column: ['Concrete compressive strength(MPa, megapascals) ']
  '''
  df =pd.read_csv(r'C:/CompositeCementStrength_PredictionModel1/data/Concrete_Data.csv')
  return df

