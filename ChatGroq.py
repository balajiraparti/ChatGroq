import streamlit as st
import os
import time
from groq import Groq
from dotenv import load_dotenv
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



st.title("Chat with Groq AI")
with st.form(key="Chat"):
    st.subheader("Input:")
    input=st.text_input("Enter promp here!")
    bt=st.form_submit_button("Generate")
    if bt:
        if not input:
            st.warning("please enter the prompt first!")
        else:
            st.subheader("Output:")
            st.empty()
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": input,
                    }
                ],
                model="mistral-saba-24b",
            )
            response=chat_completion.choices[0].message.content

            response_placeholder = st.empty()
            response_text = ""
            for word in response.split():
                response_text += word + " "
                response_placeholder.markdown(response_text)
                time.sleep(0.2)
                        # st.write(response)

            
