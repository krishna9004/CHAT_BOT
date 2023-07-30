from bardapi import Bard 
import streamlit as st 
from streamlit_chat import message
import os 

os.environ["_BARD_API_KEY"] = "Ywh_FGpeDX7EtliOVuqwyQLnDzE8j6-XKOq1abWIxsPC_BQ-zkflJjbpPJdRWyKzFrQHZg."

# Function to get the response from the Bard API based on the user's input prompt
def response_api(prompt):
    # Use Bard API to get the answer
    response = Bard().get_answer(str(prompt))
    # Extract the content from the response
    message_content = response['content']
    return message_content

# Function to get user input using a Streamlit text input widget
def user_input():
    return st.text_input("Enter your prompt:")

# Initialize session_state to store past inputs and generated outputs
if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get user input
user_text = user_input()

# If the user enters a prompt, get the response using the Bard API and store the input and output in session_state
if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

# Display the chat history (past inputs and generated outputs) in reverse order
if st.session_state['generate']:
    for i, (past_text, generated_text) in enumerate(reversed(zip(st.session_state['past'], st.session_state['generate']))):
        # Display past user input with 'is_user=True' to indicate that it's the user's message
        message(past_text, is_user=True, key=f"{i}_user")
        # Display the generated response
        message(generated_text, key=str(i))
