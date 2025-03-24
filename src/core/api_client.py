#接口调用类
import requests
from src.core.config import config
from src.core.logger import logger

class APIClient:
    def __init__(self):
        self.base_url = config["api"]["base_url"]
        self.timeout = config["api"]["timeout"]

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, timeout=self.timeout)
        logger.info(f"GET {url} - Status Code: {response.status_code}")
        return response

    def post(self, endpoint, query_params=None, body_params=None):
        url = f"{self.base_url}/{endpoint}"
        # 添加 Query 参数
        if query_params:
            url += "?" + "&".join([f"{k}={v}" for k, v in query_params.items()])
        # 发送 POST 请求
        response = requests.post(url, json=body_params, timeout=self.timeout)
        logger.info(f"POST {url} - Status Code: {response.status_code}")
        return response