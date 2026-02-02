"""
LangChain Agent for Morocco Product Search
This is the main AI agent that uses LangChain to intelligently search and compare prices
"""

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from agent.langchain_tools import MOROCCO_SEARCH_TOOLS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class MoroccoSearchAgent:
    """
    LangChain-powered agent for searching products in Morocco
    This agent can reason about which stores to check and how to compare prices
    """
    
    def __init__(self, model="gpt-4", temperature=0):
        """
        Initialize the LangChain agent
        
        Args:
            model: OpenAI model to use (gpt-4, gpt-3.5-turbo, etc.)
            temperature: Temperature for the model (0 = more focused, 1 = more creative)
        """
        # Check for API key
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "OPENAI_API_KEY not found. Please create a .env file with your API key.\n"
                "Copy .env.example to .env and add your key."
            )
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Create the agent prompt
        self.prompt = self._create_prompt()
        
        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create the agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=MOROCCO_SEARCH_TOOLS,
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=MOROCCO_SEARCH_TOOLS,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=10
        )
    
    def _create_prompt(self) -> PromptTemplate:
        """Create the agent prompt template"""
        template = """You are a helpful shopping assistant specialized in finding the best prices for products in Morocco.

Your goal is to help users find products at the best prices across Moroccan e-commerce sites like Jumia, Marjane, Electroplanet, and others.

IMPORTANT: Always sort the final results from CHEAPEST to MOST EXPENSIVE.

Available Tools:
{tools}

Tool Names: {tool_names}

When a user asks to search for a product, follow this process:
1. Search multiple stores (Jumia, Marjane, and other stores)
2. Collect all the product results
3. Use the compare_prices tool to sort and display results from cheapest to most expensive
4. Highlight the best deal and potential savings
5. Offer to save results if the user wants

Format your responses in a friendly, helpful way. Always emphasize the cheapest option.

Current conversation:
{chat_history}

User: {input}

Thought: {agent_scratchpad}"""
        
        return PromptTemplate(
            input_variables=["input", "chat_history", "agent_scratchpad", "tools", "tool_names"],
            template=template
        )
    
    def search(self, product_name: str) -> str:
        """
        Search for a product using the AI agent
        
        Args:
            product_name: Name of the product to search for
            
        Returns:
            Agent's response with sorted results
        """
        query = f"Search for '{product_name}' in Morocco and show me the prices sorted from cheapest to most expensive."
        
        try:
            result = self.agent_executor.invoke({"input": query})
            return result["output"]
        except Exception as e:
            return f"Error during search: {str(e)}"
    
    def chat(self, message: str) -> str:
        """
        Have a conversation with the agent
        
        Args:
            message: User's message
            
        Returns:
            Agent's response
        """
        try:
            result = self.agent_executor.invoke({"input": message})
            return result["output"]
        except Exception as e:
            return f"Error: {str(e)}"


# Alternative: Using LangGraph for more complex workflows
class AdvancedMoroccoSearchAgent:
    """
    Advanced agent using LangGraph for complex multi-step workflows
    Uncomment and implement if you need more sophisticated reasoning
    """
    
    def __init__(self):
        """Initialize the advanced agent with LangGraph"""
        # TODO: Implement LangGraph workflow
        # This would allow for more complex decision trees and parallel processing
        pass
    
    def search_with_filters(self, product_name: str, max_price: float = None, 
                           preferred_stores: list = None):
        """
        Advanced search with filters
        
        Args:
            product_name: Product to search for
            max_price: Maximum price filter
            preferred_stores: List of preferred stores
        """
        # TODO: Implement advanced filtering logic
        pass
