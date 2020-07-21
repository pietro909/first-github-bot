import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "pietro909", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('/repos/pietro909/algorithms-coursera/issues',
              data={
                  'title': 'We got a problem',
                  'body': 'Use more emoji!',
              })

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
