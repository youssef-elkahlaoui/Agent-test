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

## 📁 Project Structure

```
Agent/
├── main.py                      # Main entry point with LangChain agent
├── .env                         # API keys (create from .env.example)
├── .env.example                 # Environment template
├── config.py                    # Configuration settings
├── agent/
│   ├── __init__.py             # Package initializer
│   ├── langchain_agent.py      # LangChain AI agent implementation
│   ├── langchain_tools.py      # Custom tools for the agent
│   ├── product_searcher.py     # Legacy search class (backup)
│   ├── scrapers.py             # Web scraping implementations
│   └── utils.py                # Utility functions
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🛠️ How the LangChain Agent Works

The agent uses **ReAct (Reasoning + Acting)** pattern:

1. **Thinks** - Analyzes what needs to be done
2. **Acts** - Uses tools to search stores
3. **Observes** - Reviews the results
4. **Reasons** - Decides next steps
5. **Responds** - Provides sorted results

### Available Tools

The agent has access to these tools:

- `search_jumia_morocco` - Search Jumia
- `search_marjane_online` - Search Marjane
- `search_other_morocco_stores` - Search other stores
- `compare_prices` - Sort and compare all results
- `save_search_results` - Save to file

## 🔧 Extending the Agent

### Adding New E-commerce Sites

Create a new tool in `agent/langchain_tools.py`:

```python
@tool
def search_new_store(product_name: str) -> str:
    """
    Search for products on NewStore Morocco.
    """
    # Your scraping logic here
    products = [...]
    return json.dumps(products)
```

Then add it to `MOROCCO_SEARCH_TOOLS` list.

## ⚙️ Configuration

### API Keys

The agent requires an OpenAI API key. Get one from [platform.openai.com](https://platform.openai.com/api-keys)

```bash
# .env file
OPENAI_API_KEY=sk-...your-key-here...
```

### Changing the LLM Model

Edit [agent/langchain_agent.py](agent/langchain_agent.py):

```python
agent = MoroccoSearchAgent(
    model="gpt-3.5-turbo",  # Cheaper, faster
    # or model="gpt-4"       # More capable, slower
    temperature=0
)
```

### Alternative LLM Providers

You can use Claude (Anthropic) or Gemini (Google) instead:

```python
# For Claude
from langchain_anthropic import ChatAnthropic
self.llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# For Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
self.llm = ChatGoogleGenerativeAI(model="gemini-pro")
```

Currently uses mock data for demonstration. To enable real scraping:

1. Review and comply with each website's terms of service
2. Implement proper scraping logic in each `_search_*` method
3. Consider using APIs where available
4. Add rate limiting to be respectful of servers

## 📦 Key Dependencies

- **LangChain** - AI agent framework
- **OpenAI** - GPT models for intelligence
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community tools
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `selenium` - Advanced web scraping
- `python-dotenv` - Environment variables

## 📝 Notes

- **AI Agent**: This uses LangChain's ReAct agent pattern with reasoning capabilities
- **API Costs**: Using GPT-4 costs money per request; GPT-3.5-turbo is cheaper
- Always respect websites' `robots.txt` and terms of service
- Consider rate limiting to avoid overloading servers
- Some sites may require authentication or have anti-scraping measures
- Prices are displayed in MAD (Moroccan Dirham)

## 🚀 Future Enhancements

- [ ] Add more Moroccan e-commerce sites
- [ ] Implement LangGraph for complex workflows
- [ ] Add price tracking over time with memory
- [ ] Add price alerts via email/SMS
- [ ] Export to CSV/Excel with pandas
- [ ] Web interface (Flask/FastAPI)
- [ ] Real-time price monitoring
- [ ] Product comparison charts and visualizations
- [ ] Multi-language support (Arabic, French, English)
- [ ] Voice interface for searching

## 📄 License

This project is for educational purposes. Make sure to comply with all applicable laws, terms of service, and API usage policies.

## 🤝 Contributing

Feel free to:

- Add support for more Moroccan e-commerce sites
- Improve the agent's reasoning capabilities
- Add new tools for the agent
- Enhance the scraping implementations
