import os
import sys
import requests


def search_renewed_smartphones(api_key: str):
    """Search Keepa for renewed smartphones and print results."""
    url = "https://api.keepa.com/search"
    params = {
        "key": api_key,
        "domain": 1,  # Amazon.com
        "term": "renewed smartphone",
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    products = data.get("products", [])
    for product in products:
        title = product.get("title")
        asin = product.get("asin")
        print(f"{title} ({asin})")


def main(argv=None):
    argv = argv or sys.argv[1:]
    api_key = os.environ.get("KEEPA_API_KEY")
    if argv:
        api_key = argv[0]
    if not api_key:
        print("Usage: keepa_renewed_smartphones.py <API_KEY>")
        print("Or set the KEEPA_API_KEY environment variable.")
        return 1
    search_renewed_smartphones(api_key)


if __name__ == "__main__":
    raise SystemExit(main())
