import pandas as pd


model_assign_df = pd.read_csv(r"data\contacts.csv", header=None, names=['id', 'Campaign', 'Product line', 'Model', 'times'])
# print(type(model_assign_df))
# print(model_assign_df.head())
model_count_series = model_assign_df.groupby(['Product line',"Model"]).count()["times"]
# print(type(model_count_series))

# print(model_count_series.head())
model_count_series = model_count_series.sort_values(ascending=False)
model_count_series.to_csv(r"output\model_count.csv")