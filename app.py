import streamlit as st
from calculator import add, subtract, multiply, divide, power, sqrt

st.title('Calculadora Simples')

operacoes = {
    'Adição (+)': add,
    'Subtração (-)': subtract,
    'Multiplicação (*)': multiply,
    'Divisão (/)': divide,
    'Potenciação (^)': power,
    'Raiz quadrada (√)': sqrt
}

opcao = st.selectbox('Escolha a operação:', list(operacoes.keys()))

if opcao == 'Raiz quadrada (√)':
    num = st.number_input('Digite o número:', format='%f')
    if st.button('Calcular'):
        try:
            resultado = sqrt(num)
            st.success(f'√{num} = {resultado}')
        except Exception as e:
            st.error(str(e))
else:
    num1 = st.number_input('Digite o primeiro número:', key='num1', format='%f')
    num2 = st.number_input('Digite o segundo número:', key='num2', format='%f')
    if st.button('Calcular'):
        try:
            resultado = operacoes[opcao](num1, num2)
            st.success(f'Resultado: {resultado}')
        except Exception as e:
            st.error(str(e)) 