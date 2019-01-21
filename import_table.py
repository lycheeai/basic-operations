import pandas as pd

def import_table(file_gen):
  first_file = next(file_gen)
  pd_csv = pd.read_csv(first_file.result)
  def extract_column(csv, col_name):
    return (PipelineSuccess(first_file.name + "/" + str(k), [v.encode("utf8")]) for k, v in enumerate(csv[col_name]))
  return [extract_column(pd_csv, i) for i in pd_csv.columns]
