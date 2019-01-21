import pandas as pd

def import_table(file_gen):
  first_file = next(file_gen)
  pd_csv = pandas.read_csv(first_file.result)
  def extract_column(csv, col_name):
    (PipelineSuccess(first_file.name + "/" + k, v.encode("utf8")) for k, v in enumerate(my_csv['id']))
  return [extract_column(pd_csv, i) for i in pd_csv.columns]
