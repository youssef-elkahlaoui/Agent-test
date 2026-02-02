"""
Morocco Product Price Search Agent - Powered by LangChain
Main entry point for the AI-powered product search agent
"""

from agent.langchain_agent import MoroccoSearchAgent
import sys


def main():
    """Main function to run the LangChain-powered product search agent"""
    print("=" * 80)
    print("🤖 Morocco Product Price Search Agent - AI Powered")
    print("=" * 80)
    print("\nThis agent uses LangChain and AI to intelligently search for products")
    print("across multiple Moroccan e-commerce sites and compare prices.\n")

    try:
        # Initialize the LangChain agent
        print("🔧 Initializing AI agent...")
        agent = MoroccoSearchAgent(model="gpt-4", temperature=0)
        print("✅ Agent ready!\n")

    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nSetup Instructions:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        print("3. Run the program again")
        return
    except Exception as e:
        print(f"\n❌ Error initializing agent: {e}")
        return

    # Interactive mode or single search
    mode = input(
        "Choose mode:\n1. Single search\n2. Interactive chat mode\nEnter choice (1 or 2): "
    ).strip()

    if mode == "2":
        # Interactive chat mode
        print("\n" + "=" * 80)
        print(
            "Interactive Chat Mode - The agent can help you find and compare products"
        )
        print("Type 'exit' or 'quit' to end the conversation")
        print("=" * 80 + "\n")

        while True:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Goodbye! Happy shopping!")
                break

            if not user_input:
                continue

            print("\n🤖 Agent: ", end="")
            response = agent.chat(user_input)
            print(response)

    else:
        # Single search mode
        product_name = input("\nEnter product name to search: ").strip()

        if not product_name:
            print("❌ Error: Product name cannot be empty")
            return

        print(f"\n🔍 AI Agent is searching for '{product_name}'...")
        print(
            "The agent will intelligently search multiple stores and compare prices.\n"
        )

        # Let the AI agent do its work
        result = agent.search(product_name)

        print("\n" + "=" * 80)
        print("AGENT RESULT:")
        print("=" * 80)
        print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Search cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        import traceback

        traceback.print_exc()
