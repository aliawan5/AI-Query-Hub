# AI-Query-Hub
AI Query Hub using Ollama 

Langchain Demo With Ollama3
This is a demo application built with Streamlit and Langchain, utilizing the Ollama3 language model for natural language processing. It provides an interface for users to interact with an AI model that responds to their queries.

Overview
The application uses the following components:

Streamlit: A framework for building interactive web applications.
Langchain: A library for managing language models and chaining them with prompts.
Ollama: A language model (Llama3) used for generating responses.
Setup
Environment Variables

Create a .env file in the root directory of your project with the following content:

dotenv
Copy code
LANGCHAIN_API_KEY=your_langchain_api_key
Replace your_langchain_api_key with your actual Langchain API key.

Run the Application

Start the Streamlit application with the following command:

bash
Copy code
streamlit run app.py
This will launch the web interface where you can enter text and receive responses from the Ollama3 model.

Code Explanation
Loading Environment Variables

The application loads environment variables from a .env file using the dotenv package.

Prompt Template

A prompt template is defined using Langchain's ChatPromptTemplate with a system message and a user query placeholder.

Streamlit UI

The Streamlit interface consists of a text input field where users can enter their questions.

Ollama LLM Setup

The Ollama language model is set up with the Ollama class and configured with the model name 'llama3'.

LLM Chain Creation

An LLMChain is created with the defined prompt template, the Ollama model, and an output parser.

Response Generation

If the user inputs a query, the chain processes the input and generates a response that is displayed on the Streamlit interface.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
