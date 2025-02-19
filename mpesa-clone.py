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

# Streamlit UI
st.title("ATM Interface")
atm = ATM()

if "balance" not in st.session_state:
    st.session_state.balance = atm.balance

st.write(f"### Current Balance: KES {st.session_state.balance}")

# Deposit Section
deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, step=100.0)
if st.button("Deposit"):
    message = atm.deposit(deposit_amount)
    st.session_state.balance = atm.balance
    st.success(message)

# Withdraw Section
withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=100.0)
if st.button("Withdraw"):
    message = atm.withdraw(withdraw_amount)
    st.session_state.balance = atm.balance
    st.success(message)

st.write(f"### Updated Balance: KES {st.session_state.balance}")
