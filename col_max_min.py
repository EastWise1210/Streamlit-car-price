import streamlit as st
import pandas as pd


def run_col_max_min():
    st.text('선택하신 컬럼을 기준으로 최대/최소 데이터 행을 보여드립니다.')

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    column_list=['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    sel_box = st.selectbox(label='컬럼을 선택하세요', options=column_list)


    if sel_box == column_list[0]:
        st.dataframe(df[df[sel_box] == df[sel_box].max()])
        st.dataframe(df[df[sel_box] == df[sel_box].min()])

    elif sel_box == column_list[1]:
        st.dataframe(df[df[sel_box] == df[sel_box].max()])
        st.dataframe(df[df[sel_box] == df[sel_box].min()])

    elif sel_box == column_list[2]:
        st.dataframe(df[df[sel_box] == df[sel_box].max()])
        st.dataframe(df[df[sel_box] == df[sel_box].min()])

    elif sel_box == column_list[3]:
        st.dataframe(df[df[sel_box] == df[sel_box].max()])
        st.dataframe(df[df[sel_box] == df[sel_box].min()])

    else :
        st.dataframe(df[df[sel_box] == df[sel_box].max()])
        st.dataframe(df[df[sel_box] == df[sel_box].min()])