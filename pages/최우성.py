import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="시험 스트레스 힐링 명언",
    page_icon="📚",
    layout="centered"
)

# 명언 목록
quotes = [
    "성공은 포기하지 않는 사람에게 찾아온다.",
    "오늘의 노력이 내일의 결과를 만든다.",
    "천천히 가도 멈추지만 않으면 된다.",
    "실패는 성공으로 가는 과정이다.",
    "지금의 공부는 미래의 나를 위한 투자다.",
    "어려운 순간도 결국 지나간다.",
    "할 수 있다고 믿는 순간 이미 반은 성공이다.",
    "노력은 배신하지 않는다.",
    "작은 발전도 큰 성장의 시작이다.",
    "끝까지 해내는 사람이 결국 이긴다."
]

tips = [
    "5분 정도 가볍게 스트레칭하기",
    "물을 한 컵 마시기",
    "10분간 휴식하기",
    "깊게 숨을 들이마시고 천천히 내쉬기",
    "좋아하는 음악 듣기",
    "잠시 산책하기"
]

# 세션 상태 초기화
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

st.title("📚 시험 스트레스 힐링 명언")

st.write("시험공부로 지칠 때 긍정적인 명언을 읽으며 마음을 다독여 보세요!")

# 기분 선택
mood = st.selectbox(
    "지금 기분은 어떤가요?",
    ["😄 좋음", "🙂 보통", "😥 조금 힘듦", "😭 매우 스트레스"]
)

# 명언 표시
st.subheader("✨ 오늘의 명언")
st.success(st.session_state.quote)

# 버튼
if st.button("새로운 명언 보기"):
    try:
        st.session_state.quote = random.choice(quotes)
        st.rerun()
    except Exception:
        st.error("명언을 불러오는 중 오류가 발생했습니다.")

# 스트레스 완화 팁
st.subheader("💡 스트레스 줄이는 팁")
st.info(random.choice(tips))

# 기분별 메시지
if mood == "😄 좋음":
    st.write("현재의 좋은 컨디션을 유지하며 공부해보세요!")
elif mood == "🙂 보통":
    st.write("꾸준히 공부하면 좋은 결과가 있을 거예요!")
elif mood == "😥 조금 힘듦":
    st.write("잠시 쉬어가도 괜찮아요. 다시 시작하면 됩니다!")
else:
    st.write("너무 무리하지 말고 충분한 휴식을 취하세요!")

st.divider()
st.caption("시험 스트레스 완화를 위한 응원 앱")
