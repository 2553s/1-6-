import streamlit as st
import random

# 1. 페이지 기본 설정 및 제목
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍕", layout="centered")
st.title("🍳 오늘 저녁 뭐 먹지?")
st.write("결정 장애가 온 당신을 위한 맞춤형 저녁 메뉴 추천 시스템!")

---

# 2. 메뉴 데이터베이스 (간단한 사전 형식)
menu_db = {
    "한식": {
        "든든하고 헤비하게": ["삼겹살 구이", "닭볶음탕", "김치찜", "부대찌개"],
        "가볍고 깔끔하게": ["비빔밥", "콩나물국밥", "생선구이 백반", "도토리묵사발"],
        "매콤하고 자극적이게": ["매운 갈비찜", "낙지볶음", "제육볶음", "떡볶이"]
    },
    "일식/중식": {
        "든든하고 헤비하게": ["돈카츠", "짜장면&탕수육", "규동(소고기덮밥)", "라멘"],
        "가볍고 깔끔하게": ["초밥", "사케동(연어덮밥)", "우동", "소바"],
        "매콤하고 자극적이게": ["마라탕", "짬뽕", "탄탄면", "마파두부"]
    },
    "양식/기타": {
        "든든하고 헤비하게": ["스테이크", "수제버거", "시카고 피자", "까르보나라"],
        "가볍고 깔끔하게": ["리코타 치즈 샐러드", "봉골레 파스타", "월남쌈", "타코"],
        "매콤하고 자극적이게": ["페퍼로니 피자(핫소스 듬뿍)", "아라비아따 파스타", "감바스 알 아히요(페페론치노 팍팍)", "인도 커리(치킨 마살라)"]
    }
}

# 3. 사용자 입력 받기 (사이드바 및 메인 화면)
st.sidebar.header("🛠️ 취향 필터")
category = st.sidebar.selectbox("종류를 선택하세요", list(menu_db.keys()))
mood = st.sidebar.radio("오늘의 기분/상태는?", ["든든하고 헤비하게", "가볍고 깔끔하게", "매콤하고 자극적이게"])

# 4. 메뉴 추천 로직
candidate_menus = menu_db[category][mood]

st.subheader(f"🔍 {category} 중 '{mood}' 메뉴를 찾으시나요?")

col1, col2 = st.columns(2)

with col1:
    if st.button("👉 딱 하나만 골라줘!", use_container_width=True):
        selected_menu = random.choice(candidate_menus)
        st.balloons() # 축하 효과
        st.success(f"오늘 저녁은 **{selected_menu}**, 너로 정했다! 🎯")

with col2:
    if st.button("📋 후보 전체 보기", use_container_width=True):
        st.info(f"추천 후보: {', '.join(candidate_menus)}")

---

# 5. 재미 요소를 위한 '진짜 아무거나' 랜덤 버튼
st.markdown("### 🎲 결정이 정말 힘들다면?")
if st.button("🔥 장르 불문! 아무거나 하나만 찍어줘", type="primary", use_container_width=True):
    # 전체 메뉴 리스트 하나로 합치기
    all_menus = []
    for cat in menu_db.values():
        for sub_list in cat.values():
            all_menus.extend(sub_list)
            
    random_all = random.choice(all_menus)
    st.snow() # 눈 내리는 효과
    st.write(f"### 🎰 운명의 메뉴: **{random_all}**")
