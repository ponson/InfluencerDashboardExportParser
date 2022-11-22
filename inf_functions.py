def get_log_column(logs, col):
    request_content = logs['request_content']
    return request_content.to_list()
