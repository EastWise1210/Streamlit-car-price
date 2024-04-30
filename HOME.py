import streamlit as st

def run_home():
    
    st.image('./image/car.png')
    st.markdown(HOME_text, unsafe_allow_html=True)
    st.markdown(test_font2, unsafe_allow_html=True)

'''
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image('./image/car.png')
    st.markdown("<h4 style='text-align:center;'>귀하의 방문을 환영합니다.</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>현실에서 무수히 많은 데이터(data)들을 마주할 수 있습니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>그리고 데이터들이 잘 가공된 정보(inforamation)를 이용하면 우리의 의사결정에 많은 도움이 됩니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>본 대시보드에서는 자동차 구매와 관련된 데이터들을 가공하여 다양한 지표들로서 사용자에게 유용한 정보들을 제공하는 것이 목적입니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center'>좌측 메뉴에서 원하시는 서비스를 선택하실 수 있습니다.</p>", unsafe_allow_html=True)
'''


HOME_text ='''
<h4 style='text-align:center;'>귀하의 방문을 환영합니다.</h4>
<p style='text-align:center;'>우리는 현실에서 무수히 많은 데이터(data)들을 마주합니다.<br>
이 데이터들을 정리하고 가공하여 상관관계를 파악하면 우리의 의사결정에 도움이 되는 정보(information)들을 얻을 수 있습니다.<br>
본 대시보드에서는 자동차 구매와 관련된 데이터들을 가공하여 사용자에게 유용한 정보를 제공하는 것이 목적입니다.<br>
좌측 메뉴에서 원하시는 서비스를 선택하실 수 있습니다.
</p>
'''


test_font2 = '''
<style>
@font-face {
    font-family: 'InkLipquid';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/InkLipquid.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

	.title_font2{
	font-family: 'InkLipquid';
	color: white;
	}
</style>
<body>
<p class="title_font2", style='text-align:center; font-size:150px'>테스트용 텍스트</p>
</body>
'''

