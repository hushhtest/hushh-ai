from langchain_hushhai import HushhAI, HushhAIModel
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

llm = HushhAI(model_slug=HushhAIModel.LLAMA32_3B, temperature=0)
print(llm.invoke([
     SystemMessage(
        content="You are a helpful assistant! Your name is Bob."
    ),
    HumanMessage(
        content="What is your name?"
    )
]))