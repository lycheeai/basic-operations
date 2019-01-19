import pandas as pd

def import_table(file_gen):
  pd.read_csv(next(file_gen))
  
  yield 
