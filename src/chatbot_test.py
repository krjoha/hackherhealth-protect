from langchain_openai import ChatOpenAI
from config import settings
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a very friendly bot, and you always give responses that are fun to read.",
        ),
        ("user", "{input}"),
    ]
)
llm = ChatOpenAI(
    model=settings.OPENAI_MODEL,
    temperature=settings.OPENAI_TEMPERATURE,
    api_key=settings.OPENAI_KEY,
)
chain = prompt | llm


def chat(user_text: str) -> str:
    message = chain.invoke({"input": user_text})
    # print(message.response_metadata)
    return message.content


if __name__ == "__main__":
    user_text = input("Enter your chat message: ")
    response = chat(user_text)
    print(response)
