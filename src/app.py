import streamlit as st

st.write("Hola mundo desde streamlit")

st.write("Esto es una aplicación hecha con streamlit")

num_1 = st.number_input("Introduce el primer numero para sumar")

num_2 = st.number_input("Introduce el segundo numero para sumar")


st.write(num_1, " + ", num_2, " = ", num_1+num_2)