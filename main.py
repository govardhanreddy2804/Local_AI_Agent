from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

def main():
    print("✅ Local AI Pizza Review Bot is starting...\n(Type 'q' to quit)\n")

    model = OllamaLLM(model="llama3.2")  # You can also try llama3:8b

    template = """
    You are an expert in answering questions about a pizza restaurant.

    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    while True:
        question = input("\n🍕 Ask your question: ")
        if question.lower() == "q":
            break

        reviews = retriever.invoke(question)
        result = chain.invoke({"reviews": reviews, "question": question})
        print("\n🤖 Answer:")
        print(result)

if __name__ == "__main__":
    print("✅ Script loaded!")
    main()
