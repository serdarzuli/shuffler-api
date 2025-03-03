import aiohttp

async def send_get_request(url, headers=None, params=None, ssl_context=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=ssl_context) as response:
            return await response.json()

async def send_post_request(url, payload, headers=None, ssl_context=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers, ssl=ssl_context) as response:
            return await response.json()
