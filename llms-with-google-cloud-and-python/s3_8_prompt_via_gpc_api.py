import os
import vertexai
from vertexai.language_models import ChatModel

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mitch/Projects/proj_123_vertex_ai/fantastic-sniffle/llms-with-google-cloud-and-python/.env'

vertexai.init(project="genai-prompt-w-pipeline")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2, 
    "top_p": 0.8,
    "top_k": 40,
}

model_name = "chat-bison"

model = ChatModel.from_pretrained(model_name)

#context = 'Your are a personal tutor for a 5 year old'
context = 'you are a math professer and explain topics in great detail'

chat = model.start_chat(context=context)
chat.send_message("what is machine learning?")

response = chat.send_message("what is machine learning?")


print(response.text)  # This will print the generated response from the chat model
