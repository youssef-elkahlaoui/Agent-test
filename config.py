# Configuration file for Morocco Product Search Agent

# Search settings
MAX_RESULTS_PER_STORE = 50
TIMEOUT_SECONDS = 10

# Moroccan e-commerce sites
STORES = {
    "jumia": "https://www.jumia.ma",
    "marjane": "https://www.marjane.ma",
    # Add more stores here
}

# Currency
DEFAULT_CURRENCY = "MAD"

# Rate limiting (requests per minute)
RATE_LIMIT = 30
