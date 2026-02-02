"""
LangChain Tools for Morocco Product Search Agent
These tools are used by the LangChain agent to search for products
"""

from langchain.tools import tool
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import json


@tool
def search_jumia_morocco(product_name: str) -> str:
    """
    Search for products on Jumia Morocco e-commerce site.
    Use this tool when you need to find products and their prices on Jumia.
    
    Args:
        product_name: The name of the product to search for
        
    Returns:
        JSON string with list of products found
    """
    try:
        # Mock data for demonstration - replace with actual scraping
        products = [
            {
                "name": f"{product_name} - Model A",
                "price": 450.00,
                "currency": "MAD",
                "store": "Jumia Morocco",
                "url": "https://www.jumia.ma/example1",
                "availability": "In Stock"
            },
            {
                "name": f"{product_name} - Model B",
                "price": 350.00,
                "currency": "MAD",
                "store": "Jumia Morocco",
                "url": "https://www.jumia.ma/example2",
                "availability": "In Stock"
            }
        ]
        return json.dumps(products, ensure_ascii=False)
    except Exception as e:
        return f"Error searching Jumia: {str(e)}"


@tool
def search_marjane_online(product_name: str) -> str:
    """
    Search for products on Marjane online store.
    Use this tool when you need to find products and their prices on Marjane.
    
    Args:
        product_name: The name of the product to search for
        
    Returns:
        JSON string with list of products found
    """
    try:
        # Mock data for demonstration - replace with actual scraping
        products = [
            {
                "name": f"{product_name} - Marjane Brand",
                "price": 380.00,
                "currency": "MAD",
                "store": "Marjane",
                "url": "https://www.marjane.ma/example1",
                "availability": "In Stock"
            },
            {
                "name": f"{product_name} - Premium",
                "price": 520.00,
                "currency": "MAD",
                "store": "Marjane",
                "url": "https://www.marjane.ma/example2",
                "availability": "Limited Stock"
            }
        ]
        return json.dumps(products, ensure_ascii=False)
    except Exception as e:
        return f"Error searching Marjane: {str(e)}"


@tool
def search_other_morocco_stores(product_name: str) -> str:
    """
    Search for products on other Moroccan e-commerce stores (Electroplanet, Aswak Assalam, etc).
    Use this tool to get additional price comparisons from other stores.
    
    Args:
        product_name: The name of the product to search for
        
    Returns:
        JSON string with list of products found
    """
    try:
        # Mock data for demonstration
        products = [
            {
                "name": f"{product_name} - Store Brand",
                "price": 420.00,
                "currency": "MAD",
                "store": "Electroplanet",
                "url": "https://example.com/product",
                "availability": "In Stock"
            }
        ]
        return json.dumps(products, ensure_ascii=False)
    except Exception as e:
        return f"Error searching other stores: {str(e)}"


@tool
def compare_prices(products_json: str) -> str:
    """
    Compare prices from different products and sort them from cheapest to most expensive.
    Use this tool after collecting products from different stores.
    
    Args:
        products_json: JSON string containing list of products with prices
        
    Returns:
        Formatted comparison report with products sorted by price
    """
    try:
        products = json.loads(products_json)
        
        # Sort by price
        sorted_products = sorted(products, key=lambda x: x.get('price', float('inf')))
        
        # Format output
        result = f"\n{'='*80}\n"
        result += f"PRICE COMPARISON - {len(sorted_products)} Products Found\n"
        result += f"Sorted from CHEAPEST to MOST EXPENSIVE\n"
        result += f"{'='*80}\n\n"
        
        for idx, product in enumerate(sorted_products, 1):
            result += f"#{idx} - {product['price']:.2f} {product['currency']}\n"
            result += f"   Product: {product['name']}\n"
            result += f"   Store: {product['store']}\n"
            result += f"   Availability: {product['availability']}\n"
            result += f"   URL: {product['url']}\n"
            result += f"{'-'*80}\n"
        
        # Calculate savings
        if len(sorted_products) >= 2:
            cheapest = sorted_products[0]['price']
            most_expensive = sorted_products[-1]['price']
            savings = most_expensive - cheapest
            percentage = (savings / most_expensive) * 100
            
            result += f"\n💰 SAVINGS: Choose the cheapest option and save {savings:.2f} MAD "
            result += f"({percentage:.1f}% less than the most expensive)\n"
        
        return result
        
    except Exception as e:
        return f"Error comparing prices: {str(e)}"


@tool
def save_search_results(product_name: str, results: str) -> str:
    """
    Save search results to a JSON file for future reference.
    
    Args:
        product_name: The product that was searched
        results: The search results to save
        
    Returns:
        Confirmation message with filename
    """
    try:
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{product_name.replace(' ', '_')}_{timestamp}.json"
        
        data = {
            "product": product_name,
            "timestamp": timestamp,
            "results": results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return f"✅ Results saved to: {filename}"
        
    except Exception as e:
        return f"Error saving results: {str(e)}"


# List of all tools for the agent
MOROCCO_SEARCH_TOOLS = [
    search_jumia_morocco,
    search_marjane_online,
    search_other_morocco_stores,
    compare_prices,
    save_search_results
]
