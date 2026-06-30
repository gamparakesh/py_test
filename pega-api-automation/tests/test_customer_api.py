import requests
from unittest.mock import patch
from requests import Response


def _fake_response(status_code=200, content=b'{"result":"ok"}'):
    resp = Response()
    resp.status_code = status_code
    resp._content = content
    resp.headers['Content-Type'] = 'application/json'
    return resp


@patch('requests.post')
def test_customer_api(mock_post):
    mock_post.return_value = _fake_response()

    response = requests.post(
        "https://crm.apicom/getCustomer",
        json={"customerId": "12345"},
        headers={"Authorization": "Bearer your_token_here"}
    )

    assert response.status_code == 200
