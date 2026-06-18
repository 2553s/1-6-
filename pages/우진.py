import streamlit as st
import datetime

# 1. 페이지 설정
st.set_page_config(
    page_title="시험 스트레스 케어 플래너",
    page_icon="📚",
    layout="centered"
)

# 2. 메인 타이틀
st.title("📚 시험 스트레스 케어 & 효율 플래너")
st.write("스트레스는 낮추고 공부 효율은 높이는 맞춤형 시간 관리 도구입니다.")
st.markdown("---")

# 3. [기능 1] 스트레스 지수 측정
st.subheader("🧘‍♂️ 1단계: 현재 스트레스 지수 체크")
stress_score = st.slider(
    "지금 시험 공부로 인해 느끼는 스트레스는 어느 정도인가요?",
    min_value=0, max_value=100, value=50, step=5
)

# 스트레스에 따른 조언 메시지 분기 (안정적인 if문 구조)
if stress_score >= 80:
    st.error("🚨 **현재 심한 압박감을 느끼고 계시네요!**\n\n지금은 무리하게 달리면 번아웃이 옵니다. 공부 중간에 의도적으로 긴 휴식 시간을 배치해야 합니다. 목표를 조금 낮추고 하나씩 해결해 나가세요.")
    rest_modifier = 15  # 휴식 시간 추가
elif stress_score >= 50:
    st.warning("⚠️ **적당한 긴장과 불안이 있는 상태입니다.**\n\n공부 시작 전 가벼운 스트레칭이나 심호흡을 추천합니다. 계획을 세분화하여 눈에 보이게 완수해 나가는 것이 불안 해소에 도움이 됩니다.")
    rest_modifier = 10
else:
    st.success("✅ **아주 건강한 심리 상태를 유지하고 계십니다!**\n\n적절한 긴장감은 집중력을 도와줍니다. 현재 페이스를 그대로 유지하며 효율적으로 시간을 배분해 보세요.")
    rest_modifier = 5

st.markdown("---")

# 4. [기능 2] 공부 시간 효율 설계 (원하는 기능 반영)
st.subheader("⏳ 2단계: 효율적인 하루 공부 시간 계산기")
st.write("남은 시험 일정과 과목, 그리고 위의 스트레스 지수를 종합하여 최적의 뽀모도로(집중/휴식) 계획을 짜드립니다.")

# 안전한 입력 폼(Form) 구성
with st.form(key="planner_form"):
    # 시험 날짜 입력 (기본값: 오늘부터 7일 뒤)
    exam_date = st.date_input("🗓️ 시험 시작일", datetime.date.today() + datetime.timedelta(days=7))
    
    # 하루 공부 가능 시간
    study_hours = st.number_input("⏰ 하루에 공부할 수 있는 총 시간 (시간 단위)", min_value=1, max_value=16, value=4, step=1)
    
    # 과목 입력
    subjects_raw = st.text_input("📝 공부해야 할 과목들을 입력하세요 (쉼표로 구분)", value="국어, 수학, 영어")
    
    # 제출 버튼
    submit_button = st.form_submit_button(label="🚀 맞춤형 효율 플랜 생성")

# 5. 결과 출력 및 예외 처리
if submit_button:
    today = datetime.date.today()
    days_left = (exam_date - today).days
    
    # 예외 처리: 과거 날짜를 선택한 경우
    if days_left < 0:
        st.error("❌ 에러: 시험 날짜는 오늘 또는 오늘 이후여야 합니다. 날짜를 다시 확인해 주세요.")
    else:
        # 과목 텍스트 분리 및 공백 제거
        subject_list = [sub.strip() for sub in subjects_raw.split(",") if sub.strip()]
        
        if not subject_list:
            st.warning("⚠️ 과목을 최소 1개 이상 입력해 주세요.")
        else:
            st.info(f"🎉 **시험까지 남은 기간: {days_left}일**")
            
            # 스트레스 기반 집중/휴식 시간 동적 세팅
            focus_time = 25  # 기본 집중 시간 25분
            rest_time = rest_modifier  # 스트레스에 따라 5분, 10분, 15분으로 변동
            
            total_minutes = study_hours * 60
            one_cycle = focus_time + rest_time
            total_cycles = int(total_minutes // one_cycle)
            
            if total_cycles == 0:
                total_cycles = 1
                
            # 과목당 배분
            num_subjects = len(subject_list)
            cycles_per_subject = max(1, round(total_cycles / num_subjects))
            
            # 대시보드 시각화
            st.markdown("### 🎯 당신을 위한 초효율 시간 배분안")
            
            col1, col2 = st.columns(2)
            col1.metric("1회 집중 시간", f"{focus_time}분")
            col2.metric("1회 필수 휴식", f"{rest_time}분")
            
            st.write(f"👉 하루 총 **{total_cycles}번의 세션**을 수행하는 것을 추천합니다.")
            st.write("---")
            st.markdown("#### 📋 과목별 세부 가이드")
            
            for subject in subject_list:
                st.write(f"📘 **{subject}**")
                st.write(f"- 하루에 **{cycles_per_subject}번 세션** 수행하기")
                st.write(f"- 방법: `[{focus_time}분 집중] ➡️ [{rest_time}분 폰 보지 않고 휴식]` 패턴 반복")
                st.write("")
                
            st.success("💪 계획대로 다 못 지켜도 괜찮습니다. 스트레스 받지 말고 지금 할 수 있는 만큼만 시작하세요!")
