import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-06-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
)

response = client.embeddings.create(
    input = "GAA",
    model= "text-embedding-ada-002"
)

result = response.model_dump_json(indent=2)

print(result)

with open("GAA_azure.json", "w", encoding="utf-8") as file:
    file.write(result)
