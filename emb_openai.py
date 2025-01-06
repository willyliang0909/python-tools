from openai import OpenAI
import dotenv

dotenv.load_dotenv()

client = OpenAI()

response = client.embeddings.create(
    input = "GAA",
    model= "text-embedding-ada-002"
)

result = response.model_dump_json(indent=2)

print(result)

with open("GAA_openai.json", "w", encoding="utf-8") as file:
    file.write(result)
