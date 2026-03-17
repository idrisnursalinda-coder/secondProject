import streamlit as st

st.title("Welcome GUI App")
st.write("This is my first graphical interface")

name = st.text_input("Enter your name")

if st.button("Click Me"):
    st.write("Button clicked!")

num1 = st.number_input("Number 1", value=0, step=1)
num2 = st.number_input("Number 2", value=0, step=1)

if st.button("Add Numbers"):
    sum_result = num1 + num2
    st.write(f"The sum is: {sum_result}")

show_greeting = st.checkbox("Show Greeting")
if show_greeting:
    st.write("Have a nice day!")

if st.button("Submit"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello!")
    
    total = num1 + num2
    st.write(f"The sum of your numbers is {total}.")
    
    if show_greeting:
        st.write("Have a nice day!")