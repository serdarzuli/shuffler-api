# main.py
import asyncio
from src.api import ShufflerAPI
from src.config import TOKEN


async def main():
    api = ShufflerAPI(TOKEN)

    apps = await api.get_apps()
    print("Apps:", apps)

    workflows = await api.get_list_workflows()
    print("Workflows:", workflows)

if __name__ == "__main__":
    asyncio.run(main())
