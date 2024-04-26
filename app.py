
import streamlit as st
from HOME import run_home
from ML import run_ml
from EDA import run_eda
from More_about import run_more_about

#from tkinter.tix import COLUMN
#from pyparsing import empty


st.set_page_config(layout="wide")
#empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
#empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
#empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
#empyt1,con5,con6,empty2 = st.columns([0.3,0.5,0.5,0.3])


#st.markdown("""
#<style>
#	empty1{text-align:center;}
#</style>
#""", unsafe_allow_html=True)





def main() :
    st.markdown("<h1 style='text-align: center;'>자동차 구매예측</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Prediction about Car Purchasing Total</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>자동차 구매와 관련된 데이터프레임을 이용하여 다양한 정보 및 구매 예측 서비스를 제공합니다.</p>", unsafe_allow_html=True)
    menu = ['HOME', 'EDA', 'ML', 'More about']
    user_sel1 = st.sidebar.selectbox(label='SELECT', options=menu)


    if user_sel1 == menu[0]:
        run_home()

    elif user_sel1 == menu[1]:
        run_eda()
   
    elif user_sel1 == menu[2]:
        run_ml()

    else :
        run_more_about()
   


if __name__ == '__main__':
    main()





