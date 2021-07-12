import pandas as pd


model_assign_df = pd.read_csv(r"data\contacts.csv")
model_count_df = model_assign_df.groupby(["campaign", "model"]).count()
print(model_count_df)
model_count_df.to_csv(r"output\model_assignments_count.csv")