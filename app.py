
import streamlit as st
from HOME import run_home
from ML import run_ml
from EDA import run_eda
from More_about import run_more_about



def main():
    st.title('자동차 구매예측')
    st.subheader('Prediction about Car Purchasing Total')

    menu = ['HOME', 'EDA', 'ML', 'More about']
    user_sel = st.sidebar.selectbox(label='SELECT', options=menu)


    if user_sel == menu[0]:
        run_home()

    elif user_sel == menu[1]:
        run_eda()
   
    elif user_sel == menu[2]:
        run_ml()

    else :
        run_more_about()







if __name__ == '__main__':
    main()

