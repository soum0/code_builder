from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-120b")

from pydantic import BaseModel

#fixed github














class Schema(BaseModel):
    price : float
    eps : float

resp = llm.with_structured_output(Schema).invoke('Extract price and eps from this text: "The price is 100.5 and the eps is 5.6"')
print(resp)

response = llm.invoke('what you know about cricket')