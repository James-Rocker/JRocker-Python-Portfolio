import profile
import re

import cProfile
import pstats

import httpx
import asyncio

"""
Maybe we want to see what is actually taking so long when a script is running. We can do this by either using the
profiler when running the script, e.g. python3 -m cProfile common_practices/profiling.py

Or by declaring within the script. We can do this with either cProfile or profile class and chaining the run method
with a string of what we want to run
"""

profile.run('re.compile("foo|bar")')

"""
That's cool, but seems limiting for longer scripts. Instead, we can also use the profiler as a context manager. 
Let's look back at the better_count_https_in_web_pages and try running it through the profile to see what takes so long
"""


async def better_count_https_in_web_pages():
    urls = [
        "https://google.com",
        "https://youtube.com",
        "https://facebook.com",
        "https://amazon.com",
        "https://yahoo.com",
        "https://wikipedia.org",
        "https://zoom.us",
        "https://live.com",
        "https://reddit.com",
        "https://netflix.com",
        "https://microsoft.com",
        "https://office.com",
        "https://instagram.com",
        "https://msn.com",
        "https://bing.com",
    ]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url, follow_redirects=True) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print("finished parsing")
    print(f"{count_https=}")
    print(f"{count_http=}")
    print(f"{count_https/count_http=}")


with cProfile.Profile() as pr:
    asyncio.run(better_count_https_in_web_pages())

stats = pstats.Stats(pr)  # pstats allows the reporting of stats
stats.sort_stats(pstats.SortKey.TIME)  # sort it by the total time taken
stats.print_stats()  # print it to the console
# stats.dump_stats(filename="needs_profiling.prof")  # if we want to save this to a file, we can use dump_stats
