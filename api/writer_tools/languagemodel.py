import os
import dotenv
from pathlib import Path
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

llm = AzureChatOpenAI(
    api_key=os.getenv("WRITER_TOOLS_API_KEY"),
    azure_endpoint=os.getenv("WRITER_TOOLS_ENDPOINT"),
    azure_deployment=os.getenv("WRITER_TOOLS_MODEL_DEPLOYMENT"),
    api_version="2023-05-15",  # This is the released version of the API
)


def read_prompt(name: str) -> str:
    prompt_path = Path(__file__).parent / "prompts" / f"{name}.txt"

    with open(prompt_path, "r") as f:
        return f.read()


def generate_conclusion(content: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", read_prompt("system-prompt")),
            ("user", read_prompt("generate-conclusion")),
        ]
    )

    return (prompt | llm).invoke({"content": content}).content


def generate_introduction(content: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", read_prompt("system-prompt")),
            ("user", read_prompt("generate-introduction")),
        ]
    )

    return (prompt | llm).invoke({"content": content}).content
