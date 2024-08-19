# instructor_openai_embedding
client to call instructor model hosted in a openai-compatibale endpoint
# installation
```
python -m pip install "instructor_openai_embedding @ git+https://github.com/cpwan/instructor_openai_embedding"
```

# Usage
## Langchain
```python
from InstructorOpenAIEmbeddings import InstructorOpenAIEmbeddings

openai_api_key='Your API Key'
openai_api_base='http://your_own_endpoint'
tiktoken_enabled=False
tiktoken_model_name='hkunlp/instructor-xl'
embeddings = InstructorOpenAIEmbeddings(openai_api_key=openai_api_key, 
                                        openai_api_base=openai_api_base, 
                                        tiktoken_enabled=tiktoken_enabled, 
                                        tiktoken_model_name=tiktoken_model_name)
query_result = embeddings.embed_query('What is the capital of France?')
documents_result = embeddings.embed_documents(['The capital of France is Paris.', 'Barack Obama was the president of the United States.', 'France is a country in Europe.'])
print(query_result)
print(documents_result)
```
## openai
```python
import openai
client = openai.OpenAI(
    api_key='Your API Key'
    base_url='http://your_own_endpoint'
)

response = client.embeddings.create(
    model="hkunlp/instructor-xl",
    input="Hello, world!",
    extra_body={"embed_type": "query"}
)
print(response.data[0].embedding)
```

## LiteLLM
```python
import openai
client = openai.OpenAI(
    api_key='Your API Key'
    base_url='http://your_litellm_endpoint' 
)

response = client.embeddings.create(
    model="hkunlp/instructor-xl",
    input="Hello, world!",
    extra_body={"extra_body":{"embed_type": "query"}} # required for LiteLLM 
)
print(response.data[0].embedding)
```

