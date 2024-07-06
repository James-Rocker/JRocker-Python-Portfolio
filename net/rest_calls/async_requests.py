import httpx
import asyncio
import re


# async before the function declaring this function needs to be run through the asyncio runner
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

    # creates an async client, similar to the requests.session
    async with httpx.AsyncClient() as client:
        # generates a list of tasks
        tasks = (
            client.get(url, follow_redirects=True) for url in urls
        )  # creates the requests task as iterable
        reqs = await asyncio.gather(
            *tasks
        )  # runs the tasks iterables, gathers the output of these tasks to a list

    htmls = [
        req.text for req in reqs
    ]  # We can then loop through the list of sites to get the page text

    # we are just going to count the number http and https links
    count_https = 0
    count_http = 0

    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))
    print(f"https link count is: {count_https}")
    print(f"http link count is: {count_http}")


if __name__ == "__main__":
    # the async runner to actually execute the async function
    asyncio.run(better_count_https_in_web_pages())
