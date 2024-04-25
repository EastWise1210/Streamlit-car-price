import streamlit as st


def run_ml():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>2. 머신러닝</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>ML(Machine Learning)</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>머신러닝은 AI(Artificial Intellegence ,인공지능)의 연구 분야 중 하나입니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>머신러닝 기술을 이용하여 생성한 모델로 데이터에 대한 분류(classification), 예측(prediction), 군집화(clustering) 등의 작업을 수행할 수 있습니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>본 모델은 지도 학습(Supervised Learning)을 통한 예측(Prediction) 작업을 수행합니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>이 메뉴에서는 사용자에게 자동차 구매에 대한 예측 정보를 제공하며, 하단의 선택메뉴 중 사용자의 입력 값에 따라 예측 값이 변합니다.<br></p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)




    st.subheader('자동차 가격 예측하기')
    
    #1. 유저 입력값 받기
    st.text('성별을 선택하세요')
    gender = st.radio(label='성별 선택', options=['남성', '여성'])
    if gender == '남성':
        gender = 1
    elif gender == '여성':
        gender = 0

    st.text('나이를 입력하세요')
    age = st.number_input(label='나이 입력', min_value=18, max_value=110, value=28, step=1)

    st.text('연봉을 입력하세요')
    an_sal = st.number_input(label='연봉 입력', min_value=18000, value=24000)

    st.text('카드 빚을 입력하세요')
    card_debt = st.number_input(label='카드빚 입력', min_value=0)

    st.text('자산을 입력하세요')
    net_worth = st.number_input(label='자산 입력', min_value=0)


    #버튼으로 동작
    button = st.button(label='예측하기')
    if button == True:

    #2. 입력값을 바탕으로 예측하기
    #2-1. 모델 불러오기
        import joblib
        regressor = joblib.load('./model/regressor.pkl')

    #2-2. 입력값 데이터 가공
        import numpy as np
        new_data = [gender, age, an_sal, card_debt, net_worth]
        new_data = np.array(new_data).reshape(1, -1)

    #2-3. 모델의 predict 수행
        y_pred = regressor.predict(new_data)

        y_pred1 = y_pred[0]
        y_pred2 = round(y_pred1)

        y_pred3 = format(y_pred2, ",")

        st.text(f'상단에 입력하신 정보에 대한 자동차 구매금액 예측값은 {y_pred3} 달러입니다.') #첫번째 방법
        st.text(f'상단에 입력하신 정보에 대한 자동차 구매금액 예측값은 {y_pred2:,} 달러입니다.') #두번째 방법
    #첫번째와 두번째 방법 모두 같은 결과 도출

    else:
        pass










