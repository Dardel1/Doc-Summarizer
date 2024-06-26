import streamlit as st
from transformers import pipeline

summarizer = pipeline('summarization', model="facebook/bart-large-cnn")


def main():
    st.title("Document Summarizer")
    st.write("Enter your text or upload a file to get a summary:")

    user_input = st.text_area("Enter text here", height=300)
    uploaded_file = st.file_uploader("Upload a text file", type="txt")

    if uploaded_file is not None:
        user_input = uploaded_file.read().decode("utf-8")

    max_length = st.slider("Max length of summary", 50, 300, 150)
    min_length = st.slider("Min length of summary", 10, 100, 30)

    if st.button("Summarize"):
        if user_input:
            summary = summarizer(user_input, max_length=max_length, min_length=min_length, do_sample=False)
            st.write("Summary:")
            st.write(summary[0]['summary_text'])
        else:
            st.write("Please enter text or upload a file to summarize")


if __name__ == "__main__":
    main()
