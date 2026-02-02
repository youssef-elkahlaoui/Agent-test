"""
Product Search Agent
Main agent class for searching products and comparing prices
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import json
from datetime import datetime


class ProductSearchAgent:
    """Agent class for searching products in Morocco e-commerce sites"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.results = []
        
    def search_products(self, product_name: str) -> List[Dict]:
        """
        Search for products across multiple Moroccan e-commerce sites
        
        Args:
            product_name: Name of the product to search
            
        Returns:
            List of product dictionaries sorted by price (cheapest first)
        """
        all_products = []
        
        # Search on different platforms
        # Note: These are example structures - actual implementation needs real site scraping
        all_products.extend(self._search_jumia(product_name))
        all_products.extend(self._search_marjane(product_name))
        all_products.extend(self._search_generic(product_name))
        
        # Sort by price (cheapest to most expensive)
        sorted_products = sorted(all_products, key=lambda x: x['price'])
        
        return sorted_products
    
    def _search_jumia(self, product_name: str) -> List[Dict]:
        """Search Jumia Morocco"""
        products = []
        try:
            # Example placeholder - replace with actual Jumia Morocco API/scraping
            print("  → Searching Jumia...")
            # Actual implementation would scrape or use API here
            
        except Exception as e:
            print(f"  ✗ Error searching Jumia: {str(e)}")
        
        return products
    
    def _search_marjane(self, product_name: str) -> List[Dict]:
        """Search Marjane online"""
        products = []
        try:
            print("  → Searching Marjane...")
            # Actual implementation would scrape or use API here
            
        except Exception as e:
            print(f"  ✗ Error searching Marjane: {str(e)}")
        
        return products
    
    def _search_generic(self, product_name: str) -> List[Dict]:
        """Generic search method - add more stores here"""
        products = []
        try:
            print("  → Searching other stores...")
            # Example mock data for demonstration
            products = [
                {
                    'name': f'{product_name} - Basic Model',
                    'price': 299.99,
                    'currency': 'MAD',
                    'store': 'Store A',
                    'url': 'https://example.com/product1',
                    'availability': 'In Stock'
                },
                {
                    'name': f'{product_name} - Premium Model',
                    'price': 499.99,
                    'currency': 'MAD',
                    'store': 'Store B',
                    'url': 'https://example.com/product2',
                    'availability': 'In Stock'
                },
                {
                    'name': f'{product_name} - Standard',
                    'price': 399.99,
                    'currency': 'MAD',
                    'store': 'Store C',
                    'url': 'https://example.com/product3',
                    'availability': 'Limited Stock'
                }
            ]
        except Exception as e:
            print(f"  ✗ Error in generic search: {str(e)}")
        
        return products
    
    def save_results(self, results: List[Dict], product_name: str):
        """
        Save search results to a JSON file
        
        Args:
            results: List of product dictionaries
            product_name: Name of the searched product
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{product_name.replace(' ', '_')}_{timestamp}.json"
        
        data = {
            'search_query': product_name,
            'timestamp': timestamp,
            'total_results': len(results),
            'products': results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
