"""
Example scraper implementation for Moroccan e-commerce sites
This module contains example scrapers - customize based on actual site structure
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time


class ScraperBase:
    """Base class for all scrapers"""
    
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def get_page(self, url: str):
        """Fetch a web page with error handling"""
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None


class JumiaScraper(ScraperBase):
    """Scraper for Jumia Morocco"""
    
    BASE_URL = "https://www.jumia.ma"
    
    def search(self, product_name: str) -> List[Dict]:
        """
        Search for products on Jumia Morocco
        
        Args:
            product_name: Product to search for
            
        Returns:
            List of product dictionaries
        """
        products = []
        
        try:
            # Example search URL structure - adjust based on actual site
            search_url = f"{self.BASE_URL}/catalog/?q={product_name.replace(' ', '+')}"
            
            response = self.get_page(search_url)
            if not response:
                return products
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Example parsing - CUSTOMIZE based on actual HTML structure
            # This is a template - you need to inspect the actual site
            product_items = soup.find_all('article', class_='prd')  # Example class
            
            for item in product_items[:10]:  # Limit to top 10
                try:
                    # Extract product details - CUSTOMIZE selectors
                    name_elem = item.find('h3', class_='name')
                    price_elem = item.find('div', class_='prc')
                    link_elem = item.find('a', class_='core')
                    
                    if name_elem and price_elem:
                        # Extract and clean price
                        price_text = price_elem.get_text(strip=True)
                        price = self._extract_price(price_text)
                        
                        product = {
                            'name': name_elem.get_text(strip=True),
                            'price': price,
                            'currency': 'MAD',
                            'store': 'Jumia',
                            'url': self.BASE_URL + link_elem['href'] if link_elem else '',
                            'availability': 'Check Store'
                        }
                        products.append(product)
                        
                except Exception as e:
                    print(f"Error parsing product: {e}")
                    continue
            
            # Be respectful - add delay
            time.sleep(1)
            
        except Exception as e:
            print(f"Error scraping Jumia: {e}")
        
        return products
    
    def _extract_price(self, price_text: str) -> float:
        """Extract numeric price from text"""
        try:
            # Remove currency symbols and spaces
            price_clean = price_text.replace('DH', '').replace('MAD', '').replace(',', '').strip()
            return float(price_clean)
        except:
            return 0.0


class MarjaneScraper(ScraperBase):
    """Scraper for Marjane Online"""
    
    BASE_URL = "https://www.marjane.ma"
    
    def search(self, product_name: str) -> List[Dict]:
        """
        Search for products on Marjane
        
        Args:
            product_name: Product to search for
            
        Returns:
            List of product dictionaries
        """
        products = []
        
        try:
            # Example search URL - adjust based on actual site
            search_url = f"{self.BASE_URL}/search?q={product_name.replace(' ', '+')}"
            
            response = self.get_page(search_url)
            if not response:
                return products
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Example parsing - CUSTOMIZE based on actual HTML structure
            product_items = soup.find_all('div', class_='product-item')  # Example class
            
            for item in product_items[:10]:
                try:
                    name_elem = item.find('div', class_='product-name')
                    price_elem = item.find('span', class_='price')
                    link_elem = item.find('a')
                    
                    if name_elem and price_elem:
                        price_text = price_elem.get_text(strip=True)
                        price = self._extract_price(price_text)
                        
                        product = {
                            'name': name_elem.get_text(strip=True),
                            'price': price,
                            'currency': 'MAD',
                            'store': 'Marjane',
                            'url': link_elem['href'] if link_elem else '',
                            'availability': 'Check Store'
                        }
                        products.append(product)
                        
                except Exception as e:
                    print(f"Error parsing product: {e}")
                    continue
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error scraping Marjane: {e}")
        
        return products
    
    def _extract_price(self, price_text: str) -> float:
        """Extract numeric price from text"""
        try:
            price_clean = price_text.replace('DH', '').replace('MAD', '').replace(',', '').strip()
            return float(price_clean)
        except:
            return 0.0


# Example usage
if __name__ == "__main__":
    print("Testing scrapers...")
    
    # Test Jumia scraper
    jumia = JumiaScraper()
    results = jumia.search("laptop")
    print(f"Jumia found {len(results)} products")
    
    # Test Marjane scraper
    marjane = MarjaneScraper()
    results = marjane.search("laptop")
    print(f"Marjane found {len(results)} products")
