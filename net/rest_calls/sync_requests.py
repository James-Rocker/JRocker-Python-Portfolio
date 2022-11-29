from typing import Iterator, Dict, Any
import requests


def iter_beers_from_api(page_size: int = 5) -> Iterator[Dict[str, Any]]:
    # creates a request session
    session = requests.Session()
    page = 1
    while True:
        params = {"page": page, "per_page": page_size}
        response = session.get(
            "https://api.punkapi.com/v2/beers", params=params
        )  # performs a get request with params
        response.raise_for_status()  # raises error responses
        resp_data = response.json()  # get the data response from the API
        if not resp_data:
            break

        yield from resp_data
        page += 1


if __name__ == "__main__":
    beers = iter_beers_from_api()  # declare the generator to a variable
    print(
        f"single beer printing {next(beers)}"
    )  # printing the first object in the generator iterator

    for each in range(5):
        try:
            print(f"range loops: {next(beers)}")
        except StopIteration:
            break

    # The cool thing about generators is that, even though we already printed some objects, the generator remembers
    # the index, so when we loop through the generator here, it just keeps going
    for beer in beers:
        print(beer)
