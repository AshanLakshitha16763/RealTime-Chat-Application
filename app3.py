import streamlit as st
from transformers import pipeline

# Load the Hugging Face model (use @st.cache to prevent reloading on every keystroke)
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline('text-generation', model='gpt2', device=0)

model = load_model()

# Title of the app
st.title("Real-Time Text Autocompletion")

# Input box where the user types
user_input = st.text_input("Start typing your text:", "")

# We want to update the suggestions every time the input text changes
if user_input:
    # Generate predictions after every keystroke
    completions = model(user_input, max_length=len(user_input) + 20, num_return_sequences=1)
    
    # Extract the first generated completion
    predicted_text = completions[0]['generated_text']

    # Find the part of the prediction that comes after the input
    autocomplete_suggestion = predicted_text[len(user_input):]

    # Show real-time suggestion inline with the input
    st.write(f"Your text: {user_input}")
    st.write(f"Prediction: {user_input} *{autocomplete_suggestion}*")