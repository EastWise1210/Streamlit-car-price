
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



'''
AWS 클라우드 서버 서비스 이용하기 위해서,
1. 먼저는 리소스가 필요 -> EC2 : 서버 역할을 해줄 가상의 컴퓨터
2. EC2에 기본적으로 OS 설치까지 되어있음
3. 작동할 소프트웨어 -> 파이썬 설치, 아나콘다 설치
4. 




정리 : AWS 배포를 위해 EC2라는 하드웨어 자원을 할당받고
이 1. 빈 깡통에  2. OS설치  3. 구동을 위한 APP(파이썬, 아나콘다)  4. 가상환경 생성(numpy, pandas, matplotlib 등 관련 라이브러리 모두 인스톨)
5. 구성된 환경에 소스코드 업로드

※5번에서 소스코드 업로드 할 때 어떻게?  -->  원격 레포지토리를 EC2에 클론하고 pull하면 코드 적재 완료


과정
AWS 콘솔 로그인  -->  EC2(클라우드 가상 서버) 서비스 선택  -->  리전(Asia - Seoul) 선택(확인)  -->  인스턴스 시작

-->  이름 및 태그 탭에서 이름 입력  -->  어플리케이션 및 os이미지 : Amazon Linux 선택  -->  선택 후 하단 메뉴에서 프리티어 사용 가능한 유형으로 선택
-->  인스턴스 유형 : t2(프리티어 사용 가능 버전)  -->  키 페어(보안 장치) : 새로운 키 페어 생성 : 키페어 이름, 유형, 키 파일 형식 지정
-->  스토리지 구성 : 볼륨 30  -->  프로세스 시작
※주의 : 키파일은 재발급 안 됨  -->  키 파일 분실시 해당 서버에 접속하는 다른 방법 아예 X : 서버 삭제하고 새로운 서버 다시 개설해야 함

-->  모든 인스턴스 보기로 확인  -->  EC2 리소스 생성 및 OS 설치가 완료 되었으면 서버의 환경 조성을 위해서 응용 프로그램 설치 위해 원격 접속해야 함
-->  LINUX는 OpenSSH  /  WINDOWS는 PuTTY : 내 컴퓨터에 PuTTY 설치  -->  



1. PuTTY :  Session - host name란에 발급 받은 aws EC2 퍼블릭 ip주소 입력
            connection - SSH - Auth - Credentials : 발급 받은 프라이빗 키 파일(ppk) 연결
            간편 연결을 위해서 Session - save&load 이용
            설정 다 끝났으면 Open -> Login as : ec2-user 로그인
            
-------------------------------여기까지 EC2 리소스에 원격 접속 단계 완료

2. 필요한 응용 프로그램들 설치
아나콘다 리눅스 버전 프로그램의 url 주소 복사하여 원격 접속한 cmd 창에서 다운로드
url = repo.anaconda.com/archive/Anaconda3-2024.02.1-Linux-x86_64.sh
$ wget https://repo.anaconda.com/archive/Anaconda3-2024.02.1-Linux-x86_64.sh
경로는 home 디렉토리(/home/ec2-user)
$ sh Anaconda3-2024.02-1-Linux-x86_64.sh





※<AWS에서 관련 설명서(putty를 이용하여 연결)에 잘 안내되어 있음>



'''





