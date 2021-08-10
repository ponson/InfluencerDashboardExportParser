import pandas as pd


model_assign_df = pd.read_csv(r"data\contacts.csv", header=None, names=['id', 'campaign', 'model', 'time'])
model_count_series = model_assign_df.groupby(["campaign", "model"])["id"].count()
model_count_series = model_count_series.sort_values(ascending=False)
print(model_count_series.head())
model_count_series.to_csv(r"output\model_assignments_count.csv")