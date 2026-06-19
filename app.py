import streamlit as st


# -------------------------
# 페이지 설정
# -------------------------

st.set_page_config(
    page_title="시험 스트레스 분석기",
    page_icon="📊",
    layout="centered"
)


# -------------------------
# 데이터
# -------------------------

solutions = {
    "공부량 부담": [
        "공부 목표를 작은 단위로 나눠보세요.",
        "오늘 해야 할 것 3개만 먼저 정해보세요."
    ],

    "성적 걱정": [
        "결과보다 현재 할 수 있는 행동에 집중해보세요.",
        "틀리는 것은 공부 과정의 일부입니다."
    ],

    "잠 부족": [
        "잠들기 전 30분은 공부 대신 휴식 시간을 가져보세요.",
        "수면 시간을 확보하면 집중력도 좋아집니다."
    ],

    "부모님/주변 기대": [
        "혼자 고민하지 말고 마음을 이야기해보세요.",
        "자신의 목표와 다른 사람의 기대를 구분해보세요."
    ],

    "시간 부족": [
        "중요한 과목부터 우선순위를 정해보세요.",
        "짧은 시간이라도 집중해서 시작해보세요."
    ]
}


# -------------------------
# 제목
# -------------------------

st.title("📊 시험 스트레스 원인 분석기")

st.write(
    "시험기간 현재 스트레스 점수를 확인하고 "
    "스트레스를 만드는 원인을 찾아보세요."
)


st.divider()


# -------------------------
# 점수 입력
# -------------------------

st.subheader("1️⃣ 시험 스트레스 점수 측정")


study = st.slider(
    "공부량 때문에 부담을 느끼나요?",
    0, 10, 5
)

grade = st.slider(
    "성적이나 시험 결과가 걱정되나요?",
    0, 10, 5
)

sleep = st.slider(
    "잠이 부족하거나 피곤한가요?",
    0, 10, 5
)

pressure = st.slider(
    "주변 기대 때문에 압박을 느끼나요?",
    0, 10, 5
)

time = st.slider(
    "시간이 부족하다고 느끼나요?",
    0, 10, 5
)


# -------------------------
# 원인 선택
# -------------------------

st.subheader("2️⃣ 가장 큰 스트레스 원인 선택")

reasons = st.multiselect(
    "해당되는 것을 모두 선택하세요",
    list(solutions.keys())
)


# -------------------------
# 분석 버튼
# -------------------------

if st.button("📈 내 스트레스 분석하기"):

    try:

        score = int(
            (
                study
                + grade
                + sleep
                + pressure
                + time
            )
            / 50
            * 100
        )


        st.divider()

        st.subheader("결과")


        if score < 35:
            st.success(
                f"현재 스트레스 점수: {score}점\n\n"
                "비교적 안정적인 상태입니다."
            )

        elif score < 70:
            st.warning(
                f"현재 스트레스 점수: {score}점\n\n"
                "스트레스 관리가 필요한 상태입니다."
            )

        else:
            st.error(
                f"현재 스트레스 점수: {score}점\n\n"
                "휴식과 주변 도움을 함께 고려해보세요."
            )


        # 원인 분석

        st.subheader("🔎 스트레스 원인 분석")


        if reasons:

            for r in reasons:
                st.write("•", r)

            main_reason = max(
                reasons,
                key=lambda x: len(solutions[x])
            )

            st.info(
                "추천 집중 관리 원인: "
                + main_reason
            )


            st.subheader("💡 추천 해결 방법")


            for r in reasons:
                for tip in solutions[r]:
                    st.write("✅", tip)

        else:
            st.info(
                "선택한 원인이 없습니다. "
                "슬라이더 결과를 참고해보세요."
            )


    except Exception:

        st.error(
            "분석 중 오류가 발생했습니다. 다시 시도해주세요."
        )


# -------------------------
# 기록장
# -------------------------

st.divider()

st.subheader("📝 시험기간 마음 기록")

memo = st.text_area(
    "현재 고민이나 생각을 적어보세요",
    placeholder="예) 수학 시험이 걱정된다..."
)


if st.button("기록 완료"):

    if memo.strip():

        st.success(
            "기록되었습니다. 마음을 정리하는 데 도움이 될 수 있어요."
        )

    else:

        st.warning(
            "내용을 입력해주세요."
        )


# -------------------------

st.divider()

st.caption(
    "이 앱은 자기 점검용 도구입니다. "
    "스트레스가 너무 오래 지속되거나 일상생활이 힘들다면 "
    "주변의 믿을 수 있는 사람에게 도움을 요청하세요."
)
