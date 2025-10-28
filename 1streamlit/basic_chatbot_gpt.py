# Streamlit 앱 실행하기
# 터미널에서 다음 명령어를 입력하세요.
# streamlit basic_chatbot.py

# 필요한 라이브러리 불러오기
import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(page_title="나의 첫 챗봇", page_icon="🤖")

# 제목 표시
st.title("🤖 나의 첫 AI 챗봇")
st.write("안녕하세요! 무엇이든 물어보세요.")

# OpenAI API 키 설정 (사이드바에서 입력받기)
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if not api_key:
    st.warning("⚠️ 왼쪽 사이드바에 API 키를 입력해주세요.")
    st.stop()  # API 키가 없으면 여기서 프로그램 중단

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# 대화 기록을 저장할 공간 만들기 (session_state 사용)
# 페이지를 새로고침해도 대화 내용이 유지됩니다
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 내용 화면에 표시하기
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

# 사용자가 메시지를 입력했을 때
if user_input:
    # 사용자 메시지를 대화 기록에 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 사용자 메시지를 화면에 표시
    with st.chat_message("user"):
        st.write(user_input)

    # AI의 응답을 화면에 표시
    with st.chat_message("assistant"):
        # 빈 공간 만들기 (여기에 AI 응답이 채워질 예정)
        message_placeholder = st.empty()

        # GPT 호출
        response = client.chat.completions.create(
            model="gpt-5-nano",  # 사용할 AI 모델
            messages=st.session_state.messages,  # 전체 대화 내역 전송
            stream=True  # 스트리밍 방식으로 응답 받기 (타이핑 효과)
        )

        # AI 응답을 조금씩 받아서 화면에 표시
        full_response = ""
        for chunk in response:
            # 응답 조각에서 텍스트 추출
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                # 화면에 현재까지 받은 응답 표시
                message_placeholder.write(full_response + "▌")

        # 최종 응답 표시
        message_placeholder.write(full_response)

    # AI 응답을 대화 기록에 추가
    st.session_state.messages.append({"role": "assistant", "content": full_response})