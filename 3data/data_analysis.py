# Streamlit 앱 실행하기
# 터미널에서 다음 명령어를 입력하세요.
# streamlit basic_chatbot.py

# 필요한 라이브러리 불러오기
import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="나의 첫 챗봇", page_icon="🤖")

# 제목 표시
st.title("🤖 나의 첫 AI 챗봇")
st.write("안녕하세요! 무엇이든 물어보세요.")

# Gemini API 키 설정 (사이드바에서 입력받기)
api_key = st.sidebar.text_input("Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if not api_key:
    st.warning("⚠️ 왼쪽 사이드바에 API 키를 입력해주세요.")
    st.stop()  # API 키가 없으면 여기서 프로그램 중단

# Gemini 클라이언트 생성
genai.configure(api_key=api_key)

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

        # <<< 1. 시스템 프롬프트 정의 >>>
        system_prompt = """
        당신은 유튜브 데이터 분석 전문가입니다.
        당신의 역할은 YouTube 데이터를 분석하여 인사이트를 도출하는 것입니다.

        데이터는 다음 4가지 출처 중 하나 또는 여러 개가 포함될 수 있습니다:
        1. get_youtube_transcript → 영상 자막 전체 텍스트
        2. search_youtube_videos → 검색된 영상 리스트 (제목, 조회수, 채널명, 좋아요 수 등)
        3. get_channel_info → 채널 기본 정보 및 최근 영상
        4. get_youtube_comments → 댓글 내용, 좋아요 수, 작성자 등

        ---

        ### 분석 단계
        1. 데이터 파악: 어떤 MCP Tool의 결과인지 식별하고, 필요시 여러 도구의 데이터를 결합해 문맥적으로 이해합니다.
        2. 요약 / 개요 생성: 자막은 핵심 주제를, 영상 리스트는 특징을, 댓글은 감성/키워드를 요약합니다.
        3. 인사이트 추출: 영상의 핵심 메시지, 타겟 시청자, 채널의 성장 방향 등을 분석합니다.
        4. 최종 출력 형태: 분석 내용을 기반으로 구체적인 유튜브 데이터 분석 보고서를 작성합니다.

        ---

        ### 주의사항
        - 데이터가 일부 누락되었을 경우, 가능한 정보만 활용하고 데이터 부족이라고 명시합니다.
        - 댓글 분석 시 욕설, 인신공격 등은 제외하고 **주요 의견의 경향성**만 반영합니다.
        - 언어는 입력 데이터의 언어(한국어/영어 등)에 맞게 동일하게 유지합니다.
        """

        # Gemini API 호출
        model = genai.GenerativeModel(
            "gemini-2.5-pro",
            system_instruction=system_prompt
        )
        
        gemini_history = [
            {"role": m["role"], "parts": [m["content"]]}
            for m in st.session_state.messages
        ]

        chat = model.start_chat(history=gemini_history)

        # 스트리밍 응답 받기
        stream = chat.send_message(user_input, stream=True)

        full_response = ""
        for chunk in stream:
            if chunk.text:
                full_response += chunk.text
                message_placeholder.write(full_response + "▌")

        message_placeholder.write(full_response)

    # AI 응답을 대화 기록에 추가
    st.session_state.messages.append({"role": "assistant", "content": full_response})