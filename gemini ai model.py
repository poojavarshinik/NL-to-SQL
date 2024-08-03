#import all the necessary libraries
import os
import google.generativeai as genai

# Set your GEMINI_API_KEY directly in the script
os.environ["GEMINI_API_KEY"] = "your actual api key"  # Replace with your actual API key

# Configure the Gemini AI with your API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the Gemini AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an SQL query generator. I will provide you with a database schema and a natural language query. Analyze the entire schema provided and generate an SQL query based on the natural language query. The query should have no error and should be in an executable manner. The natural language provided should be matched with the available data base and the result query should be generated",
)

# Start a chat session with the model
chat_session = model.start_chat(history=[])