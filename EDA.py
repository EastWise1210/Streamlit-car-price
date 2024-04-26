import streamlit as st
import pandas as pd
from col_max_min import run_col_max_min
import seaborn as sb
import matplotlib.pyplot as plt


def run_eda():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>1. 탐색적 데이터 분석</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>EDA(Exploratory Data Analysis)</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>탐색적 데이터 분석(Exploratory Data Analysis)은 모델링(modeling)에 앞서 데이터를 살피는 모든 과정을 의미합니다.<br></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>이 메뉴에서는 자동차 구매예측 데이터프레임에 대한 다양한 정보를 제공하며, 하단의 선택메뉴 중 사용자의 선택에 따라 여러 지표들을 알려드립니다.<br></p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


    radio1_list = ['데이터프레임', '통계']
    sel_radio1 = st.radio(label='1.열람할 메뉴를 선택해주세요.', options=radio1_list)
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    if sel_radio1 == radio1_list[0]:  #radio1-1. 데이터프레임 조회

        radio2_list = ['컬럼 전체 보기', '컬럼 선택 보기']
        sel_radio_second = st.radio(label='2.다음 중 선택해주세요.', options=radio2_list)

        if sel_radio_second == radio2_list[0]: #radio2-1. 컬럼 전체 보기
            st.dataframe(df)


            #상관계수 분석
            st.markdown('<br><br>', unsafe_allow_html=True)
            st.markdown('<h3 style="text-align:center;">1. 전체 상관계수 수치 분석</h3>', unsafe_allow_html=True)
            st.dataframe(df.corr(numeric_only=True))

            #상관계수 그래프
            #st.markdown('<h3 style="text-align:center;">2. 전체 상관관계 그래프</h3>', unsafe_allow_html=True)
            #fig1 = sb.pairplot(data=df, vars=df.columns)
            #st.pyplot(fig1)

            #히트맵
            st.markdown('<h3 style="text-align:center;">2. 전체 상관관계 히트맵</h3>', unsafe_allow_html=True)
            df_corr = df.corr(numeric_only=True)
            fig2 = plt.figure()
            sb.heatmap(data=df_corr, vmin=-1, vmax=1, annot=True, fmt='.1f')
            st.pyplot(fig2)




        else:                              #radio2-2. 컬럼 선택 보기
                columns = st.multiselect(label='2-1. 컬럼을 선택해주세요.', options=df.columns)
                if len(columns) != 0:
                    st.markdown('<h4 style="text-align:center;">데이터프레임</h4>', unsafe_allow_html=True)
                    st.dataframe(df[columns])
                else : 
                    pass


                st.markdown('<h4 style="text-align:center;">상관관계 분석</h4>', unsafe_allow_html=True)
                st.markdown('<p style="text-align:center;">컬럼들을 2개 이상 선택하시면, 컬럼들간의 상관계수를 보여드립니다.</p>', unsafe_allow_html=True)
                #2개 이상 선택했을 때와 그렇지 않을 때로 조건을 구분하여 개발

                #1. 상관관계 수치분석
                st.markdown('<h4 style="text-align:center;">(1) 상관계수 수치 분석</h4>', unsafe_allow_html=True)
                if len(columns) != 0:
                                    
                    z = 0
                    for i in range(len(columns)):
                        if df[columns].iloc[:,i].dtypes == 'object' :
                            z += 1
                        else :
                            pass
                    if z == len(columns):
                        st.warning('선택하신 컬럼의 데이터의 값이 1개이거나 모두 문자열이어서 상관계수를 계산할 수 없습니다.')
                    else :
                        if len(columns) >= 2:
                            st.dataframe(df.corr(numeric_only=True))
                        elif len(columns) == 1 :
                            st.warning('선택하신 컬럼의 개수가 1개라서 상관계수를 계산할 수 없습니다.')
                        else:
                            pass

                    
                else :
                    st.warning('선택하신 컬럼이 없기 때문에 상관계수를 분석할 수 없습니다.')

                #2. 상관관계 그래프
                st.markdown('<h4 style="text-align:center;">(2) 상관계수 그래프</h4>', unsafe_allow_html=True)
                z = 0
                for i in range(len(columns)):
                    if df[columns].iloc[:,i].dtypes == 'object' :
                         z += 1
                    else :
                         pass
                if z == len(columns):
                    st.warning('선택하신 컬럼이 없거나, 데이터의 값들이 모두 문자열이거나, 숫자 데이터를 가진 컬럼이 1개 뿐이어서 상관관계 산포도를 그릴 수 없습니다.')
                else :
                    if len(columns) >= 2:
                        fig1 = sb.pairplot(data=df, vars=columns)
                        st.pyplot(fig1)
                    elif len(columns) == 1 :
                        st.warning('선택하신 컬럼의 개수가 1개라서 산포도를 그릴 수 없습니다.')
                    else:
                        pass


                #3. 상관관계 히트맵
                st.markdown('<h4 style="text-align:center;">(3) 상관관계 히트맵</h4>', unsafe_allow_html=True)

                z = 0
                for i in range(len(columns)):
                    if df[columns].iloc[:,i].dtypes == 'object' :
                         z += 1
                    else :
                         pass
                if z == len(columns):
                    st.warning('선택하신 컬럼이 없거나, 데이터의 값들이 모두 문자열이거나, 숫자 데이터를 가진 컬럼이 1개 뿐이어서 상관관계 산포도를 그릴 수 없습니다.')
                else :
                    if len(columns) >= 2:
                        df_corr = df[columns].corr(numeric_only=True)
                        fig2 = plt.figure()
                        sb.heatmap(data=df_corr, vmin=-1, vmax=1, annot=True, fmt='.1f')
                        st.pyplot(fig2)
                        #fig1 = sb.pairplot(data=df, vars=columns)
                        #st.pyplot(fig1)
                    elif len(columns) == 1 :
                        st.warning('선택하신 컬럼의 개수가 1개라서 히트맵을 그릴 수 없습니다.')
                    else:
                        pass





                




    else :                            #radio1-2. 통계 조회
        st.dataframe(df.describe())

    


   



    run_col_max_min()


