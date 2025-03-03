# tests/test_api.py
import pytest
from src.api import ShufflerAPI
from src.config import TOKEN


@pytest.mark.asyncio
async def test_get_apps():
    api = ShufflerAPI(TOKEN)
    response = await api.get_apps()
    assert response is not None

@pytest.mark.asyncio
async def test_get_list_workflows():
    api = ShufflerAPI(TOKEN)
    response = await api.get_list_workflows()
    assert response is not None
