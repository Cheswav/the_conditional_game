import streamlit as st
import random

# Questions for 1st and 2nd conditionals
first_conditional_questions = [
    "If it rains tomorrow, what will you do?",
    "If you meet your favorite celebrity, what will you say?",
    "If you forget your homework, what will you tell the teacher?",
    "If you win the lottery, what will you buy?",
    "If you don’t sleep tonight, how will you feel tomorrow?"
]

second_conditional_questions = [
    "If you were invisible for a day, what would you do?",
    "If you could have dinner with any historical figure, who would it be?",
    "If you won a million dollars, how would you spend it?",
    "If you could live in any country, where would it be?",
    "If you had a superpower, what would it be?"
]

# Randomized rewards
rewards = [
    "🎉 Amazing answer! Keep it up!",
    "🌟 You're a star! Excellent job!",
    "🔥 That was fantastic! You're on fire!",
    "👍 Keep up the great work! You nailed it!",
    "🎯 Perfect! You hit the mark!",
    "🥳 Wow! You're a conditional pro!",
]

# Streamlit app
st.title("🎲 Conditional Practice Game")
st.subheader("Learn and practice your 1st and 2nd conditionals in a fun and interactive way!")

st.write("### Choose Your Question Type:")
question_type = st.radio(
    "",
    ["1st Conditional", "2nd Conditional"]
)

# Generate question
if st.button("🎯 Get a Question"):
    st.markdown("---")
    if question_type == "1st Conditional":
        question = random.choice(first_conditional_questions)
        st.write(f"**📋 (1st Conditional):** {question}")
    else:
        question = random.choice(second_conditional_questions)
        st.write(f"**📋 (2nd Conditional):** {question}")

# Input answer
st.write("### ✍️ Your Answer:")
answer = st.text_input("Type your answer here:")

# Randomized rewards logic
if answer:
    reward = random.choice(rewards)
    st.success(reward)
    
    # Add a random animation
    if random.choice([True, False]):
        st.balloons()
    else:
        st.snow()
    
    st.write("✨ Feel free to try another question!")
