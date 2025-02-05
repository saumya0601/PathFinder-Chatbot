import os
from dotenv import find_dotenv, load_dotenv
from groq import Groq
import streamlit as st

load_dotenv(find_dotenv())
client = Groq(
    api_key = os.environ.get("GROQ_API_KEY"),
)

def generate_milestone(task_description):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content": "you are a smart and polite person who helps everyone in the most easiest manner possible"
            },
            {
                "role":"user",
                "content": f"{task_description}"
            }
        ],
        model = "llama-3.3-70b-versatile",
        stream = False,
        temperature = 1.3
    )
    return chat_completion.choices[0].message.content

def main():
    streamlit_app()

def streamlit_app():
    st.title("PathFinder: Get the step guides for anything")
    text = st.text_area("Enter the task you wish to be guided for:")
    if st.button("Generate"):
        if text:
            milestones = generate_milestone(text)
            st.markdown("-------Milestones/Steps----------")
            st.write(milestones)
        else:
            st.write("Please enter something!!")

main()