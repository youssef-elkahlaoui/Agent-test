# Morocco Product Price Search Agent 🤖

An **AI-powered LangChain agent** for intelligently searching products across Moroccan e-commerce sites and comparing prices, automatically ordering results from cheapest to most expensive.

## 🌟 Features

- 🤖 **AI-Powered Agent** - Uses LangChain with GPT-4 for intelligent reasoning
- 🔍 Multi-store search across Moroccan e-commerce platforms
- 💰 Automatic price comparison (cheapest to most expensive)
- 🧠 Smart decision-making about which stores to check
- 💬 Interactive chat mode - talk to the agent naturally
- 📊 Clean formatted results display
- 💾 Save results to JSON files
- 🛒 Support for Jumia, Marjane, Electroplanet, and more

## 🚀 What Makes This Different

This is **NOT** a simple automation script. It's a **LangChain-powered AI agent** that:
- Reasons about which stores to search
- Decides the best search strategy
- Understands natural language queries
- Can engage in conversation about products
- Makes intelligent comparisons and recommendations

## 📋 Installation

1. Clone or download this project

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your API key:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## 💻 Usage

### Run the Agent

```bash
python main.py
```

### Two Modes Available:

**1. Single Search Mode** - Quick product search
**2. Interactive Chat Mode** - Have a conversation with the AI agent

### Example - Single Search

```
🤖 Morocco Product Price Search Agent - AI Powered
========================================
This agent uses LangChain and AI to intelligently search for products
across multiple Moroccan e-commerce sites and compare prices.

🔧 Initializing AI agent...
✅ Agent ready!

Choose mode:
1. Single search
2. Interactive chat mode
Enter choice (1 or 2): 1

Enter product name to search: laptop

🔍 AI Agent is searching for 'laptop'...
The agent will intelligently search multiple stores and compare prices.

[Agent starts reasoning and using tools...]
```

### Example - Interactive Chat Mode

```
You: Find me the cheapest laptop under 5000 MAD

🤖 Agent: Let me search for laptops in Morocco and find options under 5000 MAD...
[Agent searches and compares prices]

You: What about gaming laptops?

🤖 Agent: I'll search specifically for gaming laptops...
```

#1
  Product:      laptop - Basic Model
  Price:        299.99 MAD
  Store:        Store A
  Availability: In Stock
  URL:          https://example.com/product1
```

## Project Structure

```
Agent/
├── main.py                      # Main entry point
├── agent/
│   ├── __init__.py             # Package initializer
│   ├── product_searcher.py     # Main search agent class
│   └── utils.py                # Utility functions
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Extending the Agent

### Adding New E-commerce Sites

To add support for a new Moroccan e-commerce site:

1. Open `agent/product_searcher.py`
2. Add a new method following this pattern:

```python
def _search_site_name(self, product_name: str) -> List[Dict]:
    """Search SiteName Morocco"""
    products = []
    try:
        # Add your scraping logic here
        # Return products in this format:
        # {
        #     'name': 'Product Name',
        #     'price': 299.99,
        #     'currency': 'MAD',
        #     'store': 'Store Name',
        #     'url': 'https://...',
        #     'availability': 'In Stock'
        # }
    except Exception as e:
        print(f"Error: {e}")
    return products
```

3. Call the new method in `search_products()`:

```python
all_products.extend(self._search_site_name(product_name))
```

## Configuration

Currently uses mock data for demonstration. To enable real scraping:

1. Review and comply with each website's terms of service
2. Implement proper scraping logic in each `_search_*` method
3. Consider using APIs where available
4. Add rate limiting to be respectful of servers

## Dependencies

- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser
- `pandas` - Data manipulation (optional)
- `aiohttp` - Async HTTP (optional, for faster scraping)

## Notes

- Always respect websites' `robots.txt` and terms of service
- Consider rate limiting to avoid overloading servers
- Some sites may require authentication or have anti-scraping measures
- Prices are displayed in MAD (Moroccan Dirham)

## Future Enhancements

- [ ] Add more Moroccan e-commerce sites
- [ ] Implement price tracking over time
- [ ] Add price alerts
- [ ] Export to CSV/Excel
- [ ] Web interface (Flask/FastAPI)
- [ ] Real-time price monitoring
- [ ] Product comparison charts

## License

This project is for educational purposes. Make sure to comply with all applicable laws and terms of service when scraping websites.

## Contributing

Feel free to add support for more Moroccan e-commerce sites or improve the existing functionality!
