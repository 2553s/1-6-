import streamlit as st
import random

st.set_page_config(
    page_title="시험 스트레스 해소 취미 추천기",
    page_icon="📚",
    layout="centered"
)

st.title("📚 시험 스트레스 해소 취미 추천기")
st.write("시험공부로 지친 당신에게 맞는 취미를 추천해드립니다.")

# 취미 데이터
hobbies = [
    {
        "name": "산책",
        "effect": "힐링",
        "place": "실외",
        "time": "30분 이상",
        "stress": "높음",
        "difficulty": "매우 쉬움",
        "cost": "무료",
        "reason": "가벼운 걷기는 스트레스 호르몬 감소에 도움이 됩니다.",
        "mission": "집 주변을 10분 동안 걸어보세요."
    },
    {
        "name": "러닝",
        "effect": "에너지 발산",
        "place": "실외",
        "time": "30분 이상",
        "stress": "높음",
        "difficulty": "쉬움",
        "cost": "무료",
        "reason": "운동은 스트레스를 빠르게 해소하는 데 효과적입니다.",
        "mission": "15분 가볍게 뛰어보세요."
    },
    {
        "name": "그림 그리기",
        "effect": "머리 비우기",
        "place": "실내",
        "time": "30분 이상",
        "stress": "중간",
        "difficulty": "쉬움",
        "cost": "낮음",
        "reason": "창의적인 활동은 공부 스트레스에서 벗어나게 해줍니다.",
        "mission": "아무 주제나 10분 동안 자유롭게 그려보세요."
    },
    {
        "name": "독서",
        "effect": "집중력 회복",
        "place": "실내",
        "time": "30분 이상",
        "stress": "중간",
        "difficulty": "쉬움",
        "cost": "낮음",
        "reason": "좋아하는 분야의 독서는 뇌를 편안하게 해줍니다.",
        "mission": "10페이지 읽어보세요."
    },
    {
        "name": "악기 연주",
        "effect": "성취감 얻기",
        "place": "실내",
        "time": "30분 이상",
        "stress": "중간",
        "difficulty": "보통",
        "cost": "중간",
        "reason": "실력이 늘어나는 것을 체감하며 성취감을 얻을 수 있습니다.",
        "mission": "새로운 곡의 한 부분을 연습해보세요."
    },
    {
        "name": "요가",
        "effect": "힐링",
        "place": "실내",
        "time": "10~30분",
        "stress": "높음",
        "difficulty": "쉬움",
        "cost": "무료",
        "reason": "몸과 마음을 동시에 안정시키는 활동입니다.",
        "mission": "유튜브 요가 영상 10분 따라하기."
    },
    {
        "name": "종이접기",
        "effect": "집중력 회복",
        "place": "실내",
        "time": "10~30분",
        "stress": "중간",
        "difficulty": "쉬움",
        "cost": "무료",
        "reason": "손을 사용하는 활동은 잡생각을 줄여줍니다.",
        "mission": "종이학 하나 완성하기."
    },
    {
        "name": "노래 부르기",
        "effect": "에너지 발산",
        "place": "실내",
        "time": "10~30분",
        "stress": "높음",
        "difficulty": "매우 쉬움",
        "cost": "무료",
        "reason": "감정을 표현하며 스트레스를 해소할 수 있습니다.",
        "mission": "좋아하는 노래 3곡 불러보기."
    }
]

with st.form("recommend_form"):
    stress = st.slider(
        "현재 스트레스 수준",
        min_value=1,
        max_value=10,
        value=5
    )

    free_time = st.selectbox(
        "하루에 취미에 사용할 수 있는 시간",
        ["10~30분", "30분 이상"]
    )

    place = st.radio(
        "선호 활동 장소",
        ["실내", "실외", "상관없음"]
    )

    effect = st.selectbox(
        "원하는 효과",
        [
            "머리 비우기",
            "에너지 발산",
            "힐링",
            "집중력 회복",
            "성취감 얻기"
        ]
    )

    submit = st.form_submit_button("취미 추천 받기")

if submit:
    try:
        candidates = []

        for hobby in hobbies:
            score = 0

            if hobby["effect"] == effect:
                score += 3

            if hobby["time"] == free_time:
                score += 2

            if place == "상관없음":
                score += 1
            elif hobby["place"] == place:
                score += 2

            if stress >= 8 and hobby["stress"] == "높음":
                score += 2
            elif 4 <= stress < 8 and hobby["stress"] == "중간":
                score += 2

            candidates.append((score, hobby))

        candidates.sort(reverse=True, key=lambda x: x[0])

        best = candidates[0][1]

        st.success("당신에게 가장 추천하는 취미입니다!")

        st.subheader(f"🎯 {best['name']}")

        st.write(f"**추천 이유:** {best['reason']}")
        st.write(f"**시작 난이도:** {best['difficulty']}")
        st.write(f"**예상 비용:** {best['cost']}")
        st.write(f"**스트레스 해소 효과:** {best['effect']}")

        st.markdown("---")

        st.subheader("🚀 오늘의 작은 도전")
        st.info(best["mission"])

        st.markdown("---")

        extra = random.sample(
            [h["name"] for h in hobbies if h["name"] != best["name"]],
            3
        )

        st.subheader("✨ 함께 고려해볼 취미")
        for item in extra:
            st.write(f"- {item}")

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.markdown("---")

st.subheader("💡 시험공부 스트레스 관리 팁")

tips = [
    "50분 공부 후 10분 휴식을 가져보세요.",
    "잠을 줄이는 것보다 규칙적으로 자는 것이 중요합니다.",
    "하루 10분 가벼운 운동만으로도 스트레스가 감소합니다.",
    "공부 외 활동을 죄책감 없이 즐기는 것도 생산성 향상에 도움이 됩니다.",
    "완벽함보다 꾸준함을 목표로 하세요."
]

st.info(random.choice(tips))
