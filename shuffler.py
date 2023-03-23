import aiohttp

from soar_core.actions.base_action import BaseApp
from soar_core.functions import initialize_logger

logger = initialize_logger()


class App(BaseApp):
    NAME = "Shuffler"
    is_token_expiring = False
    base_url = "https://shuffler.io/api/v1/"

    def _get_auth(self):
        config = self.get_config()
        token = config["token"]
        auth = f"Bearer {token}"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Authorization": auth,
        }
        return headers

    async def get_apps(self) -> dict:
        url = f"{self.base_url}apps"
        return await self._send_get_request(url)

    async def get_list_workflow(self) -> dict:
        url = f"{self.base_url}workflows"
        return await self._send_get_request(url)

    async def get_list_workflow_execution(self, payload: dict) -> dict:
        workflow_id = payload["workflow_id"]
        url = f"{self.base_url}workflows/{workflow_id}/executions"
        return await self._send_get_request(url)

    async def create_workflow(self, payload: dict) -> dict:
        url = f"{self.base_url}workflows"
        return await self._send_post_request(url, payload)

    async def execute_workflow(self, payload: dict) -> dict:
        execution_argument = payload["execution_argument"]
        workflow_id = payload["workflow_id"]
        url = f"{self.base_url}workflows/{workflow_id}/execute"
        return await self._send_post_request(url, execution_argument)

    async def _send_post_request(self, url, payload):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=self._get_auth(), params=payload
            ) as response:
                return await response.json()

    async def _send_get_request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._get_auth()) as response:
                return await response.json()
