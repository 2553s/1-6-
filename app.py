import streamlit as st
import random

# 1. 앱 제목 설정
st.title("🍔 오늘 저녁 뭐 먹지?")
st.write("버튼을 누르면 맛있는 저녁 메뉴를 추천해 드려요!")

# 2. 메뉴 리스트 (원하는 메뉴를 마음대로 추가/삭제해도 됩니다)
menu_list = [
    "삼겹살에 소주", "매콤한 떡볶이", "바삭한 후라이드 치킨", 
    "따뜻한 국밥", "얼큰한 짬뽕과 탕수육", "신선한 초밥", 
    "고소한 까르보나라", "든든한 김치찌개", "수제버거와 감튀"
]

---

# 3. 메뉴 추천 버튼
if st.button("🎲 메뉴 추천받기", use_container_width=True):
    # 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(menu_list)
    
    # 화면에 풍선 애니메이션 효과 주기
    st.balloons()
    
    # 결과 출력
    st.success(f"오늘 저녁은 바로... **{selected_menu}** 어떠세요?")
