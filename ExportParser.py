import pandas as pd


model_assign_df = pd.read_csv(r"data\contacts.csv", header=None, names=['id', 'Campaign', 'Product line', 'Model', 'time'])
# print(type(model_assign_df))
# print(model_assign_df.head())
model_count_series = model_assign_df.groupby(["Campaign", "Model"]).count()["time"]
# print(type(model_count_series))

# print(model_count_series.head())
model_count_series = model_count_series.sort_values(ascending=False)
# print(model_count_series.index)
# print(model_count_series["PRJ_BQP_Portable PRJ_Q421", "GV30"])
# print(model_count_series["Model"])
# print(model_count_series.head())
model_count_series.to_csv(r"output\model_assignments_count.csv")