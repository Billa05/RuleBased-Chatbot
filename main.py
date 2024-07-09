import streamlit as st
import re
import nltk

from nltk.corpus import wordnet
import random

nltk.download('wordnet', quiet=True)

# Define intents and their associated keywords and responses
intents = {
    'greet': {
        'keywords': ['hello', 'hi', 'hey', 'greetings'],
        'responses': [
            "Hello! Welcome to our Web3 organization. How can I assist you today?",
            "Hi there! What can I help you with regarding our Web3 services?",
            "Greetings! How may I be of service in the world of Web3?"
        ]
    },
    'blockchain': {
        'keywords': ['blockchain', 'distributed ledger', 'decentralized'],
        'responses': [
            "Blockchain is a decentralized, distributed ledger technology that records transactions across many computers.",
            "Our organization specializes in blockchain solutions. What specific aspect are you interested in?",
            "Blockchain technology is at the core of our Web3 services. How can I explain it further?"
        ]
    },
    'smart_contracts': {
        'keywords': ['smart contracts', 'self-executing', 'automated agreements'],
        'responses': [
            "Smart contracts are self-executing contracts with the terms directly written into code.",
            "We develop and audit smart contracts. Would you like more information on our services?",
            "Smart contracts automate agreement execution in a transparent and conflict-free way. How can I elaborate?"
        ]
    },
    'crypto': {
        'keywords': ['cryptocurrency', 'crypto', 'bitcoin', 'ethereum'],
        'responses': [
            "Cryptocurrencies are digital or virtual currencies that use cryptography for security.",
            "We offer various cryptocurrency-related services. What specific area are you interested in?",
            "From Bitcoin to Ethereum, we cover a wide range of cryptocurrencies. What would you like to know?"
        ]
    },
    'defi': {
        'keywords': ['defi', 'decentralized finance', 'lending', 'borrowing'],
        'responses': [
            "DeFi, or Decentralized Finance, uses blockchain to recreate traditional financial systems.",
            "Our DeFi solutions cover lending, borrowing, and yield farming. What aspect interests you?",
            "DeFi is revolutionizing finance. How can I explain its impact and our services?"
        ]
    },
    'nft': {
        'keywords': ['nft', 'non-fungible token', 'digital art', 'collectibles'],
        'responses': [
            "NFTs (Non-Fungible Tokens) are unique digital assets verified using blockchain technology.",
            "We provide NFT creation and marketplace services. Would you like more details?",
            "NFTs are transforming digital ownership. How can I help you understand or utilize them?"
        ]
    },
    'dao': {
        'keywords': ['dao', 'decentralized autonomous organization'],
        'responses': [
            "DAOs are organizations represented by rules encoded as a computer program, often using blockchain.",
            "We assist in creating and managing DAOs. What specific information do you need?",
            "DAOs offer a new way of organizational governance. How can I explain their benefits?"
        ]
    },
    'contact': {
        'keywords': ['contact', 'reach', 'support', 'help'],
        'responses': [
            "You can reach our support team at support@web3org.com or call us at +1-123-456-7890.",
            "For personalized assistance, please email us at info@web3org.com.",
            "Our support channels are available 24/7. How would you like to get in touch?"
        ]
    },
    'fallback': {
        'responses': [
            "I'm not sure I understand. Could you please rephrase your question?",
            "I'm still learning about Web3. Could you provide more context or ask in a different way?",
            "I don't have information on that specific topic. Is there something else I can help with?"
        ]
    }
}

# Function to get synonyms
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            lem_name = re.sub(r'[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.add(lem_name)
    return list(synonyms)

# Expand keywords with synonyms
for intent, data in intents.items():
    if 'keywords' in data:
        expanded_keywords = []
        for keyword in data['keywords']:
            expanded_keywords.extend(get_synonyms(keyword))
        data['keywords'].extend(expanded_keywords)

# Function to find the best matching intent
def get_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        if 'keywords' in data:
            for keyword in data['keywords']:
                if keyword in user_input:
                    return intent
    return 'fallback'

# Streamlit UI
st.title("Web3 Organization Chatbot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know about our Web3 services?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get chatbot response
    intent = get_intent(prompt)
    response = random.choice(intents[intent]['responses'])

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})