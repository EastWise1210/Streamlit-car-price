import streamlit as st
import pandas as pd
from col_max_min import run_col_max_min


def run_eda():
    st.header('탐색적 데이터 분석')
    st.subheader('Prediction about Car Purchasing Total')
    st.text('''탐색적 데이터 분석(Exploratory Data Analysis)은
모델링(modeling)에 앞서 데이터를 살피는 모든 과정을 의미합니다.
이 메뉴에서는 자동차 구매예측 데이터프레임에 대한 다양한 정보를 제공하며,
하단의 선택메뉴 중 사용자의 선택에 따라 여러 지표들을 알려드립니다.''')

    radio1_list = ['데이터프레임', '통계']
    sel_radio1 = st.radio(label='1.열람할 메뉴를 선택해주세요.', options=radio1_list)
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    if sel_radio1 == radio1_list[0]:  #radio1-1. 데이터프레임 조회

        radio2_list = ['컬럼 전체 보기', '컬럼 선택 보기']
        sel_radio_second = st.radio(label='2.다음 중 선택해주세요.', options=radio2_list)

        if sel_radio_second == radio2_list[0]: #radio2-1. 컬럼 전체 보기
            st.dataframe(df)
        else:                              #radio2-2. 컬럼 선택 보기
                columns = st.multiselect(label='2-1. 컬럼을 선택해주세요.', options=df.columns)
                if len(columns) != 0:
                    st.dataframe(df[columns])
                    
                else : 
                    pass

    else :                            #radio1-2. 통계 조회
        st.dataframe(df.describe())



    run_col_max_min()