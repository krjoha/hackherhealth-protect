from langchain.agents import AgentExecutor, load_tools, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from config import settings

from langchain.globals import set_debug

set_debug(settings.LANGCHAIN_VERBOSE)

from langchain_core.prompts import PromptTemplate

template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

Your objective is to write a poem about the user and their favorite animal. You are supposed to all questions to the user. Once you have an answer to all questions you are done.
If the user does not answer a question, you have to rephrase the question one time and you can do this on your own without using a tool. You cannot ask the exact same question again. If the user still does not answer the question you should move on and ask the next question.

You should always use the proper format for human-tool when asking questions.

Please ask all of these questions to the use; rephrase and ask again if the user gave a confusing answer or did not answer the question but use the promting template.:
1. What is your name?
2. What did you eat for breakfast?
3. What is your favorite animal?

TOOLS:
------

Assistant has access to the following tools:

{tools}

When prompting the user for anything you MUST use the following format until you have collected all answers:
```
Thought: Do I need to use a tool? Yes
Action: {tool_names}
Action Input: [the question to ask the user]
Observation: [the users answer]
```

When you have an an answer to all 3 questions you are done, and you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your poem here]
```

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
"""


def get_user_input() -> str:
    contents = []

    try:
        line = input("> ")
    except Exception as e:
        print(f"Error: {e}")

    contents.append(line)
    return "\n".join(contents)


prompt = PromptTemplate.from_template(template)
model = ChatOpenAI(
    model=settings.OPENAI_MODEL,
    temperature=settings.OPENAI_TEMPERATURE,
    api_key=settings.OPENAI_KEY,
)

tools = load_tools(["human"], input_func=get_user_input)
agent = create_react_agent(model, tools, prompt)
memory = ConversationBufferMemory(memory_key="chat_history")
agent_executor = AgentExecutor(agent=agent, memory=memory, tools=tools, verbose=True)


def chat() -> None:

    message = agent_executor.invoke(
        {
            "input": "Begin!"
        }
    )
    print("Chatbot completed the task!")
    print(message["output"])


if __name__ == "__main__":
    chat()
