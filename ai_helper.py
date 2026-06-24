import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_summary(text):

    prompt = f"""
    Summarize the following study material in simple and easy language.

    Content:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text

def explain_topic(topic):

    prompt = f"""
    Explain the following topic in very simple language for a college student.

    Topic:
    {topic}
    """

    response = model.generate_content(prompt)

    return response.text


def generate_mcqs(text):

    prompt = f"""
    Generate 10 multiple choice questions from the following content.

    For each question provide:
    - Question
    - 4 Options
    - Correct Answer

    Content:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text


def ask_question(pdf_text, question):

    prompt = f"""
    Based on the study material below, answer the question.

    Study Material:
    {pdf_text}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text