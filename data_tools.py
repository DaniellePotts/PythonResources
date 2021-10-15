import pandas

def df_to_json(df):
  cols = df.columns
  json = []
  for index, row in df.iterrows():
    obj = {}
    for col in cols:
      obj[col] = row[col]
    json.append(obj)
  return json
