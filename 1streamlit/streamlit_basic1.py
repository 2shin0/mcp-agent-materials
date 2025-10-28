# 기본 위젯 실습
# Streamlit 앱 실행하기
# 터미널에서 다음 명령어를 입력하세요.
# streamlit streamlit_basic1.py

# 타이틀 & 설명 텍스트
import streamlit as st
st.title("📌 Streamlit 기본 위젯 실습")
st.write("이 실습에서는 다양한 Streamlit 위젯들을 체험해볼 수 있습니다.")

# 버튼
if st.button("👉 여기를 눌러보세요"):
    st.success("✅ 버튼이 눌렸어요!")
    
# 슬라이더
age = st.slider("나이를 선택하세요", 0, 100, 30)
st.write("선택한 나이:", age)

# 텍스트 입력
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"👋 안녕하세요, {name}님!")

# 숫자 입력
number = st.number_input("좋아하는 숫자를 입력하세요", value=7)
st.write(f"입력한 숫자: {number}")

# 선택 박스
color = st.selectbox("🎨 좋아하는 색깔을 골라보세요", ["빨강", "파랑", "초록", "노랑"])
st.write(f"선택한 색: {color}")

# 체크박스
agree = st.checkbox("이용 약관에 동의합니다")
if agree:
    st.write("감사합니다! 🎉")

# 라디오 버튼
animal = st.radio("🐾 좋아하는 동물은?", ["강아지", "고양이", "토끼"])
st.write(f"당신은 {animal}를(을) 좋아하시는군요!")

# 날짜 선택
import datetime
date = st.date_input("날짜를 선택하세요", datetime.date.today())
st.write("선택한 날짜:", date)

# 파일 업로드
uploaded_file = st.file_uploader("📁 파일을 업로드하세요")
if uploaded_file:
    st.success(f"{uploaded_file.name} 파일이 업로드되었습니다.")

# 이미지 표시
from PIL import Image
st.write("예시 이미지 출력")
image = Image.open("sample.png")  # sample.png 파일 필요
st.image(image, caption="샘플 이미지", use_column_width=True)

# 라인 차트
import pandas as pd
import numpy as np
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})
st.line_chart(data.set_index("x"))