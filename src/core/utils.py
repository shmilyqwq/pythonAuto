#数据驱动工具类
import pandas as pd

def load_test_data(file_path):
    if file_path.endswith(".xlsx"):
        return pd.read_excel(file_path).to_dict("records")
    elif file_path.endswith(".json"):
        return pd.read_json(file_path).to_dict("records")
    else:
        raise ValueError("Unsupported file format")