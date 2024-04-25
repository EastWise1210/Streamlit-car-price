
import streamlit as st
from HOME import run_home
from ML import run_ml
from EDA import run_eda
from More_about import run_more_about

#from tkinter.tix import COLUMN
#from pyparsing import empty


#st.set_page_config(layout="wide")
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





'''

25일 웹 대시보드 만들기 샘플 제작


st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')

st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')

st.subheader('상관관계 분석')
st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')

    #2개 이상 선택했을 때와 그렇지 않을 때로 조건을 구분하여 개발
if len(selected_columns) >= 2:
    #1. pairplot을 그린다
    #todo : 1. seaborn 외 다른 라이브러리를 이용하여 pairplot 그려보기  /  2. pairplot 말고, 반복문 이용하여 두 컬럼의 관계를 차트로 그려보기
    fig = plt.figure()
    sb.pairplot(data=df. vars=[])
    st.pyplot(fig)


    #해결책
    fig1 = sb.pairplot(data=df, vars=selected_columns)
    st.pyplot(fig1)


    #2. 상관계수를 보여준다
    st.dataframe(df[selected_columns].corr())

else :
    pass

    




머신러닝 메뉴

'''






'''
로컬에서 테스트한 다음에 이상 없으면 로컬 레퍼지토리에 커밋하고 원격 레퍼지토리에 푸쉬한다
그 다음 aws(서버) 이용하여 배포한다


라는 과정을 면접에서 꼭 답변해야 한다
'''



