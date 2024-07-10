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
            "Hello! Welcome to our Web3 organization. Feel free to explore our services.",
            "Hi there! We're here to assist you with our Web3 services.",
            "Greetings! Our Web3 services are at your disposal."
        ]
    },
    'blockchain': {
        'keywords': ['blockchain', 'distributed ledger', 'decentralized'],
        'responses': [
            "Blockchain is a decentralized, distributed ledger technology that records transactions securely.",
            "Our organization specializes in blockchain solutions, offering a range of services from development to consultancy.",
            "Blockchain technology is at the core of our Web3 services, providing secure and transparent solutions."
        ]
    },
    'smart_contracts': {
        'keywords': ['smart contracts', 'self-executing', 'automated agreements'],
        'responses': [
            "Smart contracts are self-executing contracts with the terms of the agreement directly written into code.",
            "We develop and audit smart contracts to ensure they operate securely and efficiently.",
            "Smart contracts automate agreement execution, providing a transparent and conflict-free process."
        ]
    },
    'crypto': {
        'keywords': ['cryptocurrency', 'crypto', 'bitcoin', 'ethereum'],
        'responses': [
            "Cryptocurrencies are digital currencies that use cryptography for secure transactions.",
            "We offer a variety of cryptocurrency-related services, from trading to investment advice.",
            "Our expertise covers a wide range of cryptocurrencies, ensuring secure and informed transactions."
        ]
    },
    'defi': {
        'keywords': ['defi', 'decentralized finance', 'lending', 'borrowing'],
        'responses': [
            "DeFi, or Decentralized Finance, recreates traditional financial systems with blockchain, offering secure and transparent services.",
            "Our DeFi solutions include lending, borrowing, and yield farming, designed to maximize your investments.",
            "DeFi is revolutionizing finance, providing decentralized and accessible financial services."
        ]
    },
    'nft': {
        'keywords': ['nft', 'non-fungible token', 'digital art', 'collectibles'],
        'responses': [
            "NFTs (Non-Fungible Tokens) are unique digital assets that provide proof of ownership and authenticity.",
            "We offer comprehensive NFT services, from creation to marketplace solutions.",
            "NFTs are changing the landscape of digital ownership and art, offering new opportunities for creators and collectors."
        ]
    },
    'dao': {
        'keywords': ['dao', 'decentralized autonomous organization'],
        'responses': [
            "DAOs are blockchain-based organizations that operate through smart contracts, offering a new model for collective governance.",
            "We provide support for creating and managing DAOs, leveraging blockchain for transparent and democratic operations.",
            "DAOs represent a novel approach to governance and organization, enabling decentralized decision-making."
        ]
    },
    'contact': {
        'keywords': ['contact', 'reach', 'support', 'help'],
        'responses': [
            "You can reach our support team via email at support@web3org.com or by calling us at +1-123-456-7890.",
            "For assistance, please email us at info@web3org.com. We're here to help.",
            "Our support channels are available 24/7 for any inquiries or assistance you may need."
        ]
    },
    'fallback': {
        'responses': [
            "I'm not sure I understand. Please visit our website for more information on our services.",
            "I'm still learning about Web3. For detailed information, our website offers extensive resources.",
            "I don't have information on that specific topic. Our website may have the answers you're looking for."
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

# Function to display all unique keywords
def display_keywords():
    all_keywords = set()
    for intent_data in intents.values():
        keywords = intent_data.get('keywords', [])
        all_keywords.update(keywords)
    st.subheader("Accepted Keywords")
    st.write(", ".join(sorted(all_keywords)))

# display keywords
display_keywords()


if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know about our Web3 services?"):

    st.chat_message("user").markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    intent = get_intent(prompt)
    response = random.choice(intents[intent]['responses'])
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})