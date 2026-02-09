import streamlit as st

st.title("Simple Calculator")

# Number inputs
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
with col2:
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)

# Operation selector
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate button and result
if st.button("Calculate", type="primary"):
    result = None

    if operation == "Add":
        result = num1 + num2
        symbol = "+"
    elif operation == "Subtract":
        result = num1 - num2
        symbol = "-"
    elif operation == "Multiply":
        result = num1 * num2
        symbol = "×"
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            symbol = "÷"
        else:
            st.error("Error: Cannot divide by zero!")

    if result is not None:
        st.success(f"**Result:** {num1} {symbol} {num2} = **{result}**")
