# 추가 위젯 실습
# Streamlit 앱 실행하기
# 터미널에서 다음 명령어를 입력하세요.
# streamlit streamlit_basic2.py

import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="메뉴",
        options=["홈", "프로필", "설정"],
        icons=["house", "person", "gear"],
        menu_icon="cast",
        default_index=0
    )
st.title(f"🔘 현재 선택: {selected}")
if selected == "홈":
    st.write("🏠 홈 화면입니다.")
elif selected == "프로필":
    st.write("👤 프로필 화면입니다.")
elif selected == "설정":
    st.write("⚙️ 설정 화면입니다.")
    
from streamlit_calendar import calendar
st.title("📆 Streamlit Calendar 실습")
calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,dayGridWeek,dayGridDay",
    },
    "initialView": "dayGridMonth",  # 시작 뷰: 월간 보기
}
calendar_events = [
    {
        "title": "회의",
        "start": "2025-10-15T10:00:00",
        "end": "2025-10-15T11:30:00",
    },
    {
        "title": "점심 약속",
        "start": "2025-10-16T12:00:00",
        "end": "2025-10-16T13:00:00",
    },
    {
        "title": "프로젝트 마감",
        "start": "2025-10-20T09:00:00",
        "end": "2025-10-20T17:00:00",
    },
]
calendar_state = calendar(
    events=calendar_events,
    options=calendar_options,
    key="calendar"
)