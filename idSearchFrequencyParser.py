import pandas as pd


search_id_df = pd.read_csv(r"data\logsForIDSearchFrequency20210101to20211221.csv", header=None, names=['id', 'user_id', 'path', 'ip', 'request_method', 'request_content', 'response_code', 'created_at'])
user_id_df = search_id_df[["id", "user_id"]]
print(type(user_id_df))
print(user_id_df.groupby("user_id").count())
user_id_search_df = user_id_df.groupby("user_id").count()
print(type(user_id_search_df))
user_id_search_series = user_id_search_df["id"].sort_values(ascending=False)
print(user_id_search_series)
user_id_search_series.to_csv(r"output\searchby_id_count.csv")
# model_count_series = model_assign_df.groupby(["campaign", "model"])["id"].count()
# model_count_series = model_count_series.sort_values(ascending=False)
# print(model_count_series.head())
# model_count_series.to_csv(r"output\model_assignments_count.csv")