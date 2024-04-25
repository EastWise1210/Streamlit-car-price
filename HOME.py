import streamlit as st
from utils import html_temp

def run_home():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image('./image/car.png')
    st.markdown("<h4 style='text-align:center;'>귀하의 방문을 환영합니다.</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>현실에서 무수히 많은 데이터(data)들을 마주할 수 있습니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>그리고 데이터들이 잘 가공된 정보(inforamation)를 이용하면 우리의 의사결정에 많은 도움이 됩니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>본 대시보드에서는 자동차 구매와 관련된 데이터들을 가공하여 다양한 지표들로서 사용자에게 유용한 정보들을 제공하는 것이 목적입니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>좌측 메뉴에서 원하시는 서비스를 선택하실 수 있습니다.</p>", unsafe_allow_html=True)






