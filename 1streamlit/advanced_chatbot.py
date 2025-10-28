# Streamlit 앱 실행하기
# 터미널에서 다음 명령어를 입력하세요.
# streamlit run advanced_chatbot.py

# 필요한 라이브러리 불러오기
import streamlit as st
import google.generativeai as genai

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 페이지 설정
st.set_page_config(
    page_title="나의 AI 챗봇",
    page_icon="🤖",
    layout="wide"
)

# 제목 표시
st.title("🤖 나의 AI 챗봇 Pro")
st.write("더 똑똑해진 챗봇! 아래 추천 질문을 클릭하거나 직접 질문해보세요.")

# 사이드바 설정
with st.sidebar:
    st.header("⚙️ 설정")

    # API 키 입력
    api_key = st.text_input("Gemini API 키", type="password")

    st.divider()

    # AI 모델 선택
    st.subheader("🎯 AI 모델 선택")
    model_option = st.selectbox(
        "사용할 모델을 선택하세요",
        ["gemini-2.5-flash", "gemini-2.5-pro"],
        help="flash는 빠르고, pro는 더 정확합니다."
    )

    # 온도 설정 (창의성 조절)
    st.subheader("🌡️ 창의성 조절")
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="높을수록 더 창의적이지만 덜 정확할 수 있습니다"
    )

    st.divider()

    # 대화 기록 관리
    st.subheader("💾 대화 관리")
    if st.button("🗑️ 대화 내역 지우기", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # 대화 개수 표시
    message_count = len(st.session_state.messages)
    st.info(f"현재 대화 개수: {message_count}개")

# API 키 확인
if not api_key:
    st.warning("⚠️ 왼쪽 사이드바에 API 키를 입력해주세요.")
    st.stop()

# Gemini 클라이언트 생성
genai.configure(api_key=api_key)

# 추천 질문 버튼
st.subheader("💡 추천 질문")
col1, col2, col3, col4 = st.columns(4)

# 추천 질문 목록
suggested_questions = [
    "인공지능이 뭔가요?",
    "파이썬으로 할 수 있는 것은?",
    "건강한 아침 식사 추천해줘",
    "재미있는 농담 하나 해줘"
]

# 각 열에 버튼 배치
with col1:
    if st.button(suggested_questions[0], use_container_width=True):
        st.session_state.selected_question = suggested_questions[0]

with col2:
    if st.button(suggested_questions[1], use_container_width=True):
        st.session_state.selected_question = suggested_questions[1]

with col3:
    if st.button(suggested_questions[2], use_container_width=True):
        st.session_state.selected_question = suggested_questions[2]

with col4:
    if st.button(suggested_questions[3], use_container_width=True):
        st.session_state.selected_question = suggested_questions[3]

st.divider()

# 대화 내용 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력 처리
if "selected_question" in st.session_state:
    user_input = st.session_state.selected_question
    del st.session_state.selected_question
else:
    user_input = st.chat_input("메시지를 입력하세요...")

# 사용자가 메시지를 입력했을 때
if user_input:
    # 사용자 메시지를 대화 기록에 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 사용자 메시지 화면에 표시
    with st.chat_message("user"):
        st.write(user_input)

    # AI 응답 생성 및 표시
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        with st.spinner("생각 중..."):
            try:
                # Gemini 대화 기록 형식으로 변환 (역할 이름 수정)
                gemini_history = []
                for m in st.session_state.messages[:-1]:  # 마지막 메시지(현재 입력) 제외
                    role = "model" if m["role"] == "assistant" else "user"
                    gemini_history.append({
                        "role": role,
                        "parts": [m["content"]]
                    })

                # 모델 생성 및 채팅 시작
                generation_config = genai.types.GenerationConfig(
                    temperature=temperature
                )
                model = genai.GenerativeModel(
                    model_option,
                    generation_config=generation_config
                )
                chat = model.start_chat(history=gemini_history)

                # 스트리밍 응답 받기
                response = chat.send_message(user_input, stream=True)

                full_response = ""
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        message_placeholder.write(full_response + "▌")

                message_placeholder.write(full_response)

            except Exception as e:
                st.error(f"오류가 발생했습니다: {str(e)}")
                full_response = "죄송합니다. 응답을 생성하는 중 오류가 발생했습니다."
                message_placeholder.write(full_response)

    # AI 응답을 대화 기록에 추가
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 페이지 새로고침
    st.rerun()

# 하단 안내 메시지
if len(st.session_state.messages) == 0:
    st.info("👆 위의 추천 질문을 클릭하거나, 아래에 직접 질문을 입력해보세요!")