"""
Utility functions for the product search agent
"""

from typing import List, Dict


def display_results(products: List[Dict]):
    """
    Display search results in a formatted table
    
    Args:
        products: List of product dictionaries
    """
    if not products:
        print("No products to display.")
        return
    
    print(f"\n{'=' * 100}")
    print(f"Found {len(products)} products (sorted by price - cheapest first)")
    print(f"{'=' * 100}\n")
    
    for idx, product in enumerate(products, 1):
        price_str = f"{product['price']:.2f} {product.get('currency', 'MAD')}"
        print(f"#{idx}")
        print(f"  Product:      {product['name']}")
        print(f"  Price:        {price_str}")
        print(f"  Store:        {product.get('store', 'Unknown')}")
        print(f"  Availability: {product.get('availability', 'Unknown')}")
        print(f"  URL:          {product.get('url', 'N/A')}")
        print(f"{'-' * 100}")


def format_price(price: float, currency: str = "MAD") -> str:
    """
    Format price with currency
    
    Args:
        price: Price value
        currency: Currency code (default: MAD)
        
    Returns:
        Formatted price string
    """
    return f"{price:.2f} {currency}"


def calculate_savings(products: List[Dict]) -> Dict:
    """
    Calculate potential savings by choosing cheapest option
    
    Args:
        products: List of product dictionaries
        
    Returns:
        Dictionary with savings information
    """
    if len(products) < 2:
        return {'savings': 0, 'percentage': 0}
    
    cheapest = products[0]['price']
    most_expensive = products[-1]['price']
    savings = most_expensive - cheapest
    percentage = (savings / most_expensive) * 100 if most_expensive > 0 else 0
    
    return {
        'savings': savings,
        'percentage': percentage,
        'cheapest_price': cheapest,
        'most_expensive_price': most_expensive
    }
