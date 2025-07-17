import os
import datetime
from typing import List, Dict

# The sp-api library must be installed separately.
try:
    from sp_api.api import Orders, Reports, Sellers
    from sp_api.base import SellingApiException
except ImportError:  # pragma: no cover - library might not be installed in test env
    Orders = Reports = Sellers = None  # type: ignore
    SellingApiException = Exception  # type: ignore


def get_credentials() -> Dict[str, str]:
    """Load SP API credentials from environment variables."""
    return {
        "refresh_token": os.environ.get("SP_REFRESH_TOKEN", ""),
        "lwa_app_id": os.environ.get("SP_LWA_APP_ID", ""),
        "lwa_client_secret": os.environ.get("SP_LWA_CLIENT_SECRET", ""),
        "aws_access_key": os.environ.get("SP_AWS_ACCESS_KEY", ""),
        "aws_secret_key": os.environ.get("SP_AWS_SECRET_KEY", ""),
        "role_arn": os.environ.get("SP_ROLE_ARN", ""),
    }


def fetch_orders(credentials: Dict[str, str], start: datetime.datetime, end: datetime.datetime) -> List[Dict]:
    """Fetch orders between start and end dates."""
    if Orders is None:
        raise RuntimeError("sp-api library not available")
    api = Orders(credentials=credentials)
    orders = []
    token = None
    while True:
        try:
            data = api.get_orders(CreatedAfter=start.isoformat(), CreatedBefore=end.isoformat(), NextToken=token)
        except SellingApiException as exc:  # pragma: no cover - network call
            print(f"Failed to fetch orders: {exc}")
            break
        orders.extend(data.payload.get("Orders", []))
        token = data.payload.get("NextToken")
        if not token:
            break
    return orders


def summarize_profit(orders: List[Dict]) -> float:
    """Compute total order revenue.

    This is a simplified calculation. Real profit should account for fees and costs.
    """
    total = 0.0
    for order in orders:
        amounts = order.get("OrderTotal", {})
        total += float(amounts.get("Amount", 0.0))
    return total


def summarize_best_sellers(orders: List[Dict]) -> Dict[str, int]:
    """Count order lines per ASIN."""
    best = {}
    for order in orders:
        for item in order.get("OrderItems", []):
            asin = item.get("ASIN")
            quantity = int(item.get("QuantityOrdered", 0))
            best[asin] = best.get(asin, 0) + quantity
    return best


def main() -> int:
    credentials = get_credentials()
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(days=365)

    orders = fetch_orders(credentials, start, end)
    print(f"Retrieved {len(orders)} orders")

    profit = summarize_profit(orders)
    print(f"Total revenue: ${profit:.2f}")

    best = summarize_best_sellers(orders)
    print("Best sellers:")
    for asin, qty in sorted(best.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {asin}: {qty}")

    # Placeholders for returns and claims reports. In a real application, you
    # would query the appropriate SP API endpoints here.
    print("Returns and claims reporting not implemented in this example.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
