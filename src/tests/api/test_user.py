from pathlib import Path
import pytest
from src.core.api_client import APIClient
from src.core.utils import load_test_data

# 加载测试数据
test_data_path = Path(__file__).parent.parent.parent / "data" / "api_data" / "test_data.json"
test_data = load_test_data(test_data_path)

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_user(api_client):
    response = api_client.get("users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
@pytest.mark.parametrize("data", test_data, ids=[item["name"] for item in test_data])
def test_user_login(api_client, data):
    # 获取 Query 参数和 Body 参数
    query_params = data.get("query_params", {})
    body_params = data.get("body_params", {})

    # 发送 POST 请求
    response = api_client.post("user/login", query_params=query_params, body_params=body_params)

    # 断言状态码
    assert response.status_code == data["expected_status"]

    # 断言响应消息
    response_data = response.json()
    if "expected_message" in data:
        assert data["expected_message"] in response_data.get("message", "")