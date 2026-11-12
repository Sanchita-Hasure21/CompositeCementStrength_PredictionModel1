from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing


# orchestron Layer Design : Entry Point Modeling
from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing
from src.model_build import model_build
def main(): # Function Definition
  df = data_ingestion()
  #Step2: Data preprocessing and cleaning
  X_train,X_test,y_train,y_test = data_preprocessing(df)
  score = model_build(X_train,X_test,y_train,y_test)
  print(f'R2 Score {score}')


main()# Function Calling