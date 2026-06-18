import streamlit as st
import datetime
import math

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(
    page_title="마인드 케어 시험 플래너",
    page_icon="📚",
    layout="centered"
)

# 스타일 커스텀 (따뜻하고 안정감을 주는 톤)
st.markdown("""
    <style>
    .main { background-color: #f9fbfd; }
    .stButton>button { width: 100%; background-color: #4A90E2; color: white; border-radius: 8px; }
    .stress-box { padding: 15px; border-radius: 10px; background-color: #FFF3CD; border-left: 5px solid #FFC107; margin-bottom: 15px; }
    .plan-box { padding: 15px; border-radius: 10px; background-color: #E2F0D9; border-left: 5px solid #385723; margin-bottom: 10px; }
    </style>
""", unsafe_allowed_html=True)

# 헤더 영역
st.title("📚 시험 스트레스 ZERO! 효율 중심 플래너")
st.caption("시험공부 스트레스는 줄이고, 효율은 극대화하는 당신만의 페이스메이커")

# 탭 구성으로 화면 분할 (깔끔한 UI)
tab1, tab2 = st.tabs(["🧘‍♂️ 나의 스트레스 진단", "🗓️ 효율적 공부 시간 설계"])

# -------------------------------------------------------------
# Tab 1: 스트레스 & 상태 진단
# -------------------------------------------------------------
with tab1:
    st.header("현재 내 마음 상태 체크하기")
    st.write("지금 느끼는 압박감을 솔직하게 선택해 주세요. 상태에 맞는 공부 전략을 추천해 드립니다.")
    
    stress_level = st.slider("현재 나의 시험 스트레스 지수는?", 0, 100, 50, help="위로 올릴수록 스트레스가 높음을 의미합니다.")
    
    st.markdown("---")
    st.subheader("💡 당신만을 위한 멘탈 케어 가이드")
    
    if stress_level >= 80:
        st.markdown("""
        <div class='stress-box'>
        🚨 <b>번아웃 위험 신호! 코드 레드!</b><br>
        지금은 무리하게 책상에 앉아있어도 효율이 나지 않습니다. 
        목표치를 평소의 50%로 줄이고, <b>'30분 공부, 15분 휴식'</b> 전략을 취하세요. 
        오늘 한 과목을 끝내지 못해도 괜찮습니다. 우선 순위 높은 딱 한 가지만 하세요.
        </div>
        """, unsafe_allowed_html=True)
    elif stress_level >= 50:
        st.markdown("""
        <div class='stress-box' style='background-color: #E8F4F8; border-left: 5px solid #2980B9;'>
        ⚠️ <b>불안감이 엄습하는 상태</b><br>
        시험이 다가오면서 걱정이 많아진 상태군요. 정상적인 반응입니다!<br>
        막연한 불안을 없애기 위해 <b>'시간 단위가 아닌, 분량 단위(Task-based)'</b>로 계획을 쪼개어 시각화하세요.
        </div>
        """, unsafe_allowed_html=True)
    else:
        st.markdown("""
        <div class='stress-box' style='background-color: #E2F0D9; border-left: 5px solid #27AE60;'>
        ✅ <b>좋은 긴장감 유지 중!</b><br>
        아주 이상적인 상태입니다. 적당한 긴장감은 집중력을 높여줍니다.<br>
        현재 페이스를 유지하되, 하루 1번 가벼운 스트레칭으로 척추 건강을 챙기세요!
        </div>
        """, unsafe_allowed_html=True)

    # 오늘의 확언 (Motivation)
    st.info("✨ **오늘의 한 줄:** 완벽하게 하려고 하지 마세요. 끝까지 하는 것이 완벽한 것입니다.")

# -------------------------------------------------------------
# Tab 2: 효율적 공부 시간 설계 (핵심 기능)
# -------------------------------------------------------------
with tab2:
    st.header("⏳ 맞춤형 뽀모도로 시간 설계기")
    st.write("남은 일수와 스트레스를 고려해 가장 효율적인 '집중/휴식 시간' 템플릿을 생성합니다.")
    
    # 예외 처리를 위한 폼 구성
    with st.form("planner_form"):
        col1, col2 = st.columns(2)
        with col1:
            target_date = st.date_input("🗓️ 시험 시작일", datetime.date.today() + datetime.timedelta(days=7))
        with col2:
            daily_hours = st.number_input("⏰ 하루에 공부 가능한 총 시간 (시간)", min_value=1.0, max_value=16.0, value=4.0, step=0.5)
            
        subjects_input = st.text_input("📚 공부해야 할 과목들 (쉼표로 구분)", value="수학, 영어, 한국사")
        
        submitted = st.form_submit_button("🔥 나만의 효율 플랜 계산하기")

    if submitted:
        try:
            # 예외 처리: 날짜 검증
            today = datetime.date.today()
            days_left = (target_date - today).days
            
            if days_left < 0:
                st.error("❌ 시험일은 오늘 또는 오늘 이후의 날짜여야 합니다!")
            else:
                # 과목 리스트 정제
                subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]
                
                if not subjects:
                    st.warning("⚠️ 최소 한 개 이상의 과목을 입력해 주세요.")
                else:
                    st.success(f"🎉 시험까지 **{days_left}일** 남았습니다. 최적의 루트를 제안합니다!")
                    
                    # 스트레스 지수 반영한 집중 세션 조율 (Tab 1의 값 연동)
                    if stress_level >= 80:
                        focus_time = 25  # 분
                        rest_time = 10
                    elif stress_level >= 50:
                        focus_time = 40
                        rest_time = 10
                    else:
                        focus_time = 50
                        rest_time = 10
                        
                    # 하루 총 분(minutes) 계산
                    total_minutes = daily_hours * 60
                    one_session = focus_time + rest_time
                    total_sessions = math.floor(total_minutes / one_session)
                    
                    if total_sessions == 0:
                        total_sessions = 1 # 최소 1세션 보장
                    
                    # 과목별 세션 배분
                    sub_count = len(subjects)
                    sessions_per_subject = max(1, math.ceil(total_sessions / sub_count))
                    
                    # 결과 출력 UI
                    st.markdown("### 🎯 내 스트레스 맞춤 타임블록 추천")
                    st.metric(label="하루 권장 집중 세션", value=f"{total_sessions} 세션", help=f"1세션 = 집중 {focus_time}분 + 휴식 {rest_time}분")
                    
                    st.write("---")
                    st.subheader("📋 과목별 추천 타임라인")
                    
                    for sub in subjects:
                        st.markdown(f"""
                        <div class='plan-box'>
                        📘 <b>{sub}</b>: 하루 <b>{sessions_per_subject} 세션</b> 배정<br>
                        • <span style='color:#C0392B; font-weight:bold;'>{focus_time}분 집중</span> 타이머 켜고 딴짓 금지!<br>
                        • <span style='color:#27AE60; font-weight:bold;'>{rest_time}분 휴식</span> 스트레칭 및 수분 섭취
                        </div>
                        """, unsafe_allowed_html=True)
                        
                    st.caption("※ 과목이 너무 많다면 하루에는 최대 3과목까지만 쪼개어 공부하는 것을 강력 추천합니다.")
                    
        except Exception as e:
            st.error(f"오류가 발생했습니다. 입력 값을 다시 확인해주세요. (에러: {e})")
