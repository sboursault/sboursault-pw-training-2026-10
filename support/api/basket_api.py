from base64 import b64encode

from playwright.sync_api import APIRequestContext


class BasketApi:
    def __init__(self, api_request: APIRequestContext):
        self.api_request = api_request

    def clear_basket(self, login: str, password: str):
        auth = b64encode(f"{login}:{password}".encode("utf-8")).decode("ascii")
        self.api_request.delete(
            "/api/basket/",
            headers={"Authorization": f"Basic {auth}"},
            fail_on_status_code=True,
        )
