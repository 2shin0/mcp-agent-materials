import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="나의 첫 챗봇", page_icon="🤖")

st.title("🤖 나의 첫 AI 챗봇")
st.write("안녕하세요! 무엇이든 물어보세요.")

api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")
if not api_key:
    st.warning("⚠️ 왼쪽 사이드바에 API 키를 입력해주세요.")
    st.stop()

client = OpenAI(api_key=api_key)

# ✅ system_prompt를 별도 변수로 정의
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
1. 데이터 파악
2. 요약 / 개요 생성
3. 인사이트 추출
4. 최종 출력 형태: 분석 내용을 기반으로 보고서 작성

---

### 주의사항
- 데이터 부족 시 “데이터 부족” 명시
- 댓글 분석 시 욕설·인신공격 제외
- 언어는 입력 데이터의 언어 유지
"""

# 세션 상태 초기화 (system prompt는 저장하지 않음)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # ✅ system_prompt를 여기서만 prepend
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages,
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.write(full_response + "▌")

        message_placeholder.write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
