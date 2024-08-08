# instructor_openai_embedding
client to call instructor model hosted in a openai-compatibale endpoint
# installation
```
python -m pip install "instructor_openai_embedding @ git+https://github.com/cpwan/instructor_openai_embedding"
```

# to use it in python
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