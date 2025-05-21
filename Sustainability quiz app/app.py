import streamlit as st
import random

st.title("Sustainability Quiz App")

quiz = [
    {
        "question": "What gas do trees absorb?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which of these is renewable?",
        "options": ["Coal", "Wind", "Oil", "Natural Gas"],
        "answer": "Wind"
    },
    {
        "question": "What can you compost?",
        "options": ["Plastic", "Glass", "Food Scraps", "Metal"],
        "answer": "Food Scraps"
    }
]

random.shuffle(quiz)

if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if st.session_state.q_index < len(quiz):
    q = quiz[st.session_state.q_index]
    st.subheader(q["question"])
    user_answer = st.radio("Choose one:", q["options"], key=st.session_state.q_index)

    if st.button("Submit Answer"):
        if user_answer == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! The correct answer is: {q['answer']}")
        st.session_state.q_index += 1
        st.experimental_rerun()
else:
    st.success(f"Quiz complete! Your final score: {st.session_state.score}/{len(quiz)}")
    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.experimental_rerun()