import streamlit as st

class ATM:
    def __init__(self, balance=15000):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"You have deposited KES {amount}. Your new balance is: KES {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"You have withdrawn KES {amount}. Your remaining balance is: KES {self.balance}"
        return "Invalid withdrawal amount or insufficient funds."

# Initialize session state
if "balance" not in st.session_state:
    st.session_state.balance = 15000  # Initial balance

# Display current balance
st.title("ATM Interface")
st.write(f"### Current Balance: KES {st.session_state.balance}")

# Deposit Section
deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, step=100.0)
if st.button("Deposit"):
    if deposit_amount > 0:
        st.session_state.balance += deposit_amount
        st.success(f"You have deposited KES {deposit_amount}. Your new balance is: KES {st.session_state.balance}")
    else:
        st.error("Invalid deposit amount.")

# Withdraw Section
withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=100.0)
if st.button("Withdraw"):
    if 0 < withdraw_amount <= st.session_state.balance:
        st.session_state.balance -= withdraw_amount
        st.success(f"You have withdrawn KES {withdraw_amount}. Your remaining balance is: KES {st.session_state.balance}")
    else:
        st.error("Invalid withdrawal amount or insufficient funds.")

st.write(f"### Updated Balance: KES {st.session_state.balance}")
