 import streamlit as st
import random

st.title("🐍💧🔫 Snake-Water-Gun Game")
st.write("Play against the computer!")

youstr = st.radio("Choose your move:", ["Snake 🐍", "Water 💧", "Gun 🔫"])

youDict = {"Snake 🐍": 1, "Water 💧": -1, "Gun 🔫": 0}
reverseDict = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

you = youDict[youstr]

if st.button("Play Game"):
    computer = random.choice([-1, 0, 1])

    st.write(f"👤 You chose: {reverseDict[you]}")
    st.write(f"🤖 Computer chose: {reverseDict[computer]}")

    if computer == you:
        st.info("It's a draw!")
    else:
        if computer == -1 and you == 1:
            st.success("🏆 You win!")
        elif computer == -1 and you == 0:
            st.error("💥 You lose")
        elif computer == 1 and you == -1:
            st.error("💥 You lose")
        elif computer == 1 and you == 0:
            st.success("🏆 You win!")
        elif computer == 0 and you == 1:
            st.error("💥 You lose")
        elif computer == 0 and you == -1:
            st.success("🏆 You win!")