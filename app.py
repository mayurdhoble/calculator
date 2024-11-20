import streamlit as st



num1=st.number_input("enter num1")
num2=st.number_input("enter num2")


def add():
    st.header("add is: ",num1+num2)
def sub():
    st.header("sub is: ",num1-num2)
    
def mul():
    st.header("mul is: ",num1*num2)
def div():
    if num1==0 and num2==0:
        st.header("Nothing")
    else:
      st.write("div is: ",num1/num2)
    #if num1==0 | num2==0:
      #  st.write("non divisable")



col1, col2, col3 ,col4= st.columns([1, 1, 1,1])  # Adjust width ratios as needed

with col1:
    button1 = st.button('sum')

with col2:
    button2 = st.button('sub')

with col3:
    button3 = st.button('mul')

with col4:
    button4 = st.button('div')

if button1:
    add()

if button2:
    sub()

if button3:
    mul()
if button4:
    div()
    

