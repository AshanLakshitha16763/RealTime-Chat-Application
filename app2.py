import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv



load_dotenv()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Streamlit Bot", page_icon=":shark:", layout="wide")
 
st.title("Streamlit Bot")

# get response

# def get_response(query,chat_history):
#    template = """
#                 You are helpful assistant. Answer the following questions considering the history of the conversation: 
                 
#                 call history: {chat_history}

#                 User question: {User_question}

#                 """

#    prompt = ChatPromptTemplate.from_template(template)

#    llm = ChatOpenAI() 

#    chain = prompt | llm | StrOutputParser()

#  return chain.invoke({
#        "chat_history": chat_history, 
#        "user_question": query,
#   })



# conversation

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
       with st.chat_message("Human"):
            st.markdown(message.content)
    
    else:
       with st.chat_message("AI"):
            st.markdown(message.content)


# User input

user_query = st.chat_input("Your message here.....")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = "I don't know"
        st.markdown(ai_response)

    st.session_state.chat_history.append(AIMessage(ai_response))
    