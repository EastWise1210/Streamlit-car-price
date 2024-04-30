
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

from HOME import run_home
from ML import run_ml
from EDA import run_eda
from More_about import run_more_about
from utils import html_main_head

#from tkinter.tix import COLUMN
#from pyparsing import empty


#st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,1.5,0.2])
#empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
#empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
#empyt1,con5,con6,empty2 = st.columns([0.3,0.5,0.5,0.3])


#st.markdown("""
#<style>
#	empty1{text-align:center;}
#</style>
#""", unsafe_allow_html=True)




def main() :

    #sidebar 블록
    with st.sidebar:
        option_menu_list = ['HOME', 'INTRODUCTION', 'EDA', 'MACHINE LEARNING', 'CUSTROMER SERVICE', 'ETC']
        choose = option_menu("Welcome!", option_menu_list,
                            icons=['house', 'camera fill', 'kanban'],
                            menu_icon="bi bi-emoji-smile", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#000000"},
            "icon": {"color": "orange", "font-size": "15px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )

    #메인메뉴 선택하면 해당 화면 보여주기
    if choose == option_menu_list[0]:
        run_home()
    elif choose == option_menu_list[1]:
        pass
    elif choose == option_menu_list[2]:
        run_eda()
    elif choose == option_menu_list[3]:
        run_ml()
    else :
        run_more_about()


    #column 1 블록
    with con1:
        st.markdown(html_main_head, unsafe_allow_html=True)

        #사이드바 셀렉트박스 1
        menu1_list = ['example1', 'example2', 'example3', 'example4', 'example5']
        user_side_menu1 = st.sidebar.selectbox(label='SUB SELECT EX1', options=menu1_list)
        if user_side_menu1 == menu1_list[0]:
            pass
        elif user_side_menu1 == menu1_list[1]:
            pass
    
        elif user_side_menu1 == menu1_list[2]:
            pass
        elif user_side_menu1 == menu1_list[3]:
            pass
        else :
            pass

        #사이드바 셀렉트박스 2
        menu2_list = ['example1', 'example2', 'example3', 'example4', 'example5']
        user_side_menu2 = st.sidebar.selectbox(label='SUB SELECT EX2', options=menu2_list)
        if user_side_menu2 == menu2_list[0]:
            pass

        elif user_side_menu2 == menu2_list[1]:
            pass
    
        elif user_side_menu2 == menu2_list[2]:
            pass
        elif user_side_menu2 == menu2_list[3]:
            pass
        else :
            pass


        #사이드바 셀렉트박스 3
        menu3_list = ['example1', 'example2', 'example3', 'example4', 'example5']
        user_side_menu3 = st.sidebar.selectbox(label='SUB SELECT EX3', options=menu3_list)
        if user_side_menu2 == menu2_list[0]:
            pass

        elif user_side_menu2 == menu2_list[1]:
            pass
    
        elif user_side_menu2 == menu2_list[2]:
            pass
        elif user_side_menu2 == menu2_list[3]:
            pass
        else :
            pass

        #사이드바 셀렉트박스 4
        menu4_list = ['example1', 'example2', 'example3', 'example4', 'example5']
        user_side_menu4 = st.sidebar.selectbox(label='SUB SELECT EX4', options=menu4_list)
        if user_side_menu2 == menu2_list[0]:
            pass

        elif user_side_menu2 == menu2_list[1]:
            pass
    
        elif user_side_menu2 == menu2_list[2]:
            pass
        elif user_side_menu2 == menu2_list[3]:
            pass
        else :
            pass





if __name__ == '__main__':
    main()





