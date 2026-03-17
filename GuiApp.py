import streamlit as st

# Question 1: Display title and text message
st.title("Welcome GUI App")
st.write("This is my first graphical interface")

# Question 2: Text input for name
name = st.text_input("Enter your name")

# Question 3: Button that displays message when clicked
if st.button("Click Me"):
    st.write("Button clicked!")

# Question 4: Two number inputs (no separate Add button)
num1 = st.number_input("Number 1", value=0, step=1)
num2 = st.number_input("Number 2", value=0, step=1)

# Question 5: Checkbox for greeting
show_greeting = st.checkbox("Show Greeting")

# Question 6: Submit button that combines everything
if st.button("Submit"):
    # Display hello with name
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello!")
    
    # Display sum
    total = num1 + num2
    st.write(f"The sum of your numbers is {total}.")
    
    # Display greeting if checkbox is checked
    if show_greeting:
        st.write("Have a nice day!")