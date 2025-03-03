# src/api.py
from src.auth import get_ssl_context, get_headers
from src.utils import send_get_request, send_post_request
from src.config import BASE_URL

class ShufflerAPI:
    def __init__(self, token: str):
        self.token = token
        self.ssl_context = get_ssl_context()
        self.headers = get_headers(self.token)

    async def get_apps(self):
        url = f"{BASE_URL}/apps"
        return await send_get_request(url, headers=self.headers, ssl_context=self.ssl_context)

    async def get_list_workflows(self):
        url = f"{BASE_URL}/workflows"
        return await send_get_request(url, headers=self.headers, ssl_context=self.ssl_context)

    async def get_workflow_executions(self, workflow_id: str):
        url = f"{BASE_URL}/workflows/{workflow_id}/executions"
        return await send_get_request(url, headers=self.headers, ssl_context=self.ssl_context)

    async def create_workflow(self, payload: dict):
        url = f"{BASE_URL}/workflows"
        return await send_post_request(url, payload, headers=self.headers, ssl_context=self.ssl_context)

    async def execute_workflow(self, workflow_id: str, execution_argument: dict):
        url = f"{BASE_URL}/workflows/{workflow_id}/execute"
        return await send_post_request(url, execution_argument, headers=self.headers, ssl_context=self.ssl_context)
