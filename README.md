# Web3 Organization Chatbot

This chatbot application is designed to provide information about our Web3 services using natural language processing (NLP) and Streamlit for the user interface. Below is a concise explanation of the technologies and techniques used in this project.

## Technologies Used

### Streamlit
Streamlit is used to create an interactive web-based user interface for the chatbot. It allows us to easily display chat messages, accept user input, and maintain chat history across user interactions.

### NLTK (Natural Language Toolkit)
NLTK is utilized for NLP tasks, specifically to handle and manipulate text data. In this project, it is used to download and access the WordNet corpus for finding synonyms of keywords.

### WordNet
WordNet is a lexical database of English used in this project to expand the keyword set for each intent by generating synonyms. This helps in better matching user queries to the predefined intents.

## Project Structure

- **Intents Definition**: Each intent is defined with associated keywords and responses. Intents cover various topics related to Web3 services like blockchain, smart contracts, DeFi, NFTs, DAOs, and more.

- **Synonym Expansion**: For each keyword in the intents, synonyms are generated using WordNet to create an expanded list of keywords. This improves the chatbot's ability to understand user queries.

- **Intent Matching**: User input is matched against the expanded keywords to determine the appropriate intent. If no match is found, a fallback response is provided.

- **Chat Interface**: The Streamlit-based interface displays the chat history, accepts new user inputs, and shows responses from the chatbot.
