# codex5

This repository contains a simple Python script to retrieve renewed smartphone data from the Keepa API.

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Provide your Keepa API key via environment variable or command-line argument:

```bash
export KEEPA_API_KEY="your_api_key"
python3 keepa_renewed_smartphones.py
```

or

```bash
python3 keepa_renewed_smartphones.py your_api_key
```

The script queries Keepa for "renewed smartphone" and prints the product title and ASIN for each result.

