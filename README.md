# codex5

This repository contains example Python scripts that interact with ecommerce APIs.

- `keepa_renewed_smartphones.py` retrieves renewed smartphone data from the Keepa API.
- `amazon_reports.py` shows how to fetch order information from the Amazon Selling Partner API and summarise revenue and best sellers for the last year.

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

The Amazon SP API requires additional credentials. See the script for environment variables that need to be set.

## Usage

### Keepa example

Provide your Keepa API key via environment variable or command-line argument:

```bash
export KEEPA_API_KEY="your_api_key"
python3 keepa_renewed_smartphones.py
```

or

```bash
python3 keepa_renewed_smartphones.py your_api_key
```

### Amazon reports example

Set the SP API credentials in environment variables:

```bash
export SP_REFRESH_TOKEN="..."
export SP_LWA_APP_ID="..."
export SP_LWA_CLIENT_SECRET="..."
export SP_AWS_ACCESS_KEY="..."
export SP_AWS_SECRET_KEY="..."
export SP_ROLE_ARN="..."
python3 amazon_reports.py
```

The Amazon script prints total revenue and best sellers for the last year. Returns and claims reporting are left as an exercise for the user.
