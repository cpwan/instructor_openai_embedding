from langchain_openai.embeddings.base import OpenAIEmbeddings
class InstructorOpenAIEmbeddings(OpenAIEmbeddings):
    '''
    Tested on `openai==1.37.2`
    '''
    openai_api_key: str
    openai_api_base: str
    tiktoken_enabled: bool
    tiktoken_model_name: str  # Changed from assignment to type annotation

    def embed_documents(self, input: str):
        self.model_kwargs['extra_body'] = {'embed_type':'documents'}
        # call parent method
        result = super().embed_documents(input)
        return result

    def embed_query(self,input: str):
        self.model_kwargs['extra_body'] = {'embed_type':'query'}
        result = super().embed_documents([input])[0]
        return result

if __name__ == '__main__':
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