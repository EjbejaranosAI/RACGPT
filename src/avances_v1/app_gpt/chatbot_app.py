
import openai
import streamlit as st

openai.api_key = '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'


def chatbot_app(message):
    # Make a request to the ChatGPT model
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the engine that suits your requirements
        prompt=message,
        max_tokens=100,   # Adjust the response length as needed
        temperature=0.4,  # Adjust the temperature to control randomness
        n=1,              # Generate a single response
        stop=None,        # Add custom stop conditions if needed
        timeout=10,       # Adjust the timeout as needed
    )
    # Extract the generated response
    reply = response.choices[0].text.strip()
    return reply

st.button("Es")
st.button("En")

st.write("""
# Welcome to RACGPT

""")
user_input = st.text_input("User Input")
if user_input:
    # Pass the user input to the chatbot function
    bot_reply = chatbot_app(user_input)
    st.text_area("ChatGPT", value=bot_reply, height=200)

# streamlit run chatbot_app.py
