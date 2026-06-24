import streamlit as st

st.set_page_config(
    page_title="Smart Learning Assistant Using Generative AI",
    page_icon="📚",
    layout="wide"
)

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
st.markdown("""
<div style='text-align:center;padding:10px;'>

<h1>📚 Smart Learning  Assistant Using Generative AI</h1>

<p style='font-size:20px;color:gray;'>
Transform PDFs into Summaries, MCQs and Q&A
</p>

</div>
""", unsafe_allow_html=True)
st.divider()
st.caption("Developed by Ankit Yadav | B.Sc. Computer Science")


from pdf_reader import extract_text_from_pdf
from ai_helper import (
    generate_summary,
    explain_topic,
    generate_mcqs,
    ask_question
)
load_css()



uploaded_file = st.file_uploader(
    "Upload Study Material",
    type=["pdf"]
)
st.markdown("<br>", unsafe_allow_html=True)

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    pdf_text = extract_text_from_pdf(uploaded_file)

    word_count = len(pdf_text.split())

    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Words", word_count)

    with col2:
        st.metric("📚 File Type", "PDF")

    with col3:
        st.metric("🤖 AI", "Ready")

    
    with st.expander("📄 View PDF Content"):
        st.text_area(
            "PDF Preview",
            pdf_text[:5000],
            height=300
        )

    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📄 Summary", "📘 Explain", "📝 MCQs", "❓ Q&A"]
    )

    

    with tab1:

        st.subheader("AI Summary")

        if st.button("Generate Summary", key="summary_btn"):

            with st.spinner("Generating Summary..."):

                summary = generate_summary(pdf_text)

                st.write(summary)

                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

    with tab2:

        st.subheader("Explain Topic")

        topic = st.text_input(
            "Enter Topic",
            key="topic"
        )

        if st.button(
            "Explain Topic",
            key="explain_btn"
        ):

            if topic:

                explanation = explain_topic(topic)

                st.write(explanation)

    with tab3:

        st.subheader("Generate MCQs")

        if st.button(
            "Generate MCQs",
            key="mcq_btn"
        ):

            with st.spinner("Creating MCQs..."):

                mcqs = generate_mcqs(pdf_text)

                st.write(mcqs)

    with tab4:

        st.subheader("Ask Questions From Notes")

        question = st.text_input(
            "Ask a Question",
            key="question"
        )

        if st.button(
            "Get Answer",
            key="answer_btn"
        ):

            if question:

                answer = ask_question(
                    pdf_text,
                    question
                )

                st.write(answer)