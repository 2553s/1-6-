import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="달달한 연애상담소", page_icon="💖")
st.title("💖 달달한 연애상담소")
st.caption("연애 고민, 썸, 이별 이야기까지 무엇이든 편하게 들려주세요.")

# 2. Streamlit Secrets에서 API 키 불러오기 및 클라이언트 초기화
# Streamlit Cloud에 배포할 때 지정할 secrets 키 이름을 사용합니다.
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    # 로컬 테스트용 환경변수 백업
    import os
    api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("🔑 Gemini API Key가 설정되지 않았습니다. Streamlit Secrets 설정을 확인해주세요.")
    st.stop()

# 최신 google-genai 클라이언트 생성
client = genai.Client(api_key=api_key)

# 3. 세션 상태로 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 기존 대화 기록 화면에 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 사용자 입력 받기
if prompt := st.chat_input("고민을 말해보세요... (예: 썸녀 카톡 심리가 궁금해)"):
    # 사용자 메시지 화면에 표시 및 세션 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. 챗봇 답변 생성 및 오류 처리
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # 연애 상담사 페르소나 부여를 위한 시스템 지침 설정
            system_instruction = (
                "당신은 공감 능력이 뛰어나고 위트 있는 전문 연애 상담사입니다. "
                "사용자의 고민에 깊이 공감해주고, 친구처럼 친근하면서도 현실적인 조언을 해주세요. "
                "이모지를 적절히 섞어서 따뜻한 톤앤매너를 유지하세요."
            )
            
            # 대화 맥락 유지를 위해 이전 기록을 Gemini 형식으로 변환
            # (단, 가볍고 빠른 상담을 위해 최신 대화 위주로 구성하는 것이 좋습니다)
            contents = []
            for m in st.session_state.messages:
                # google-genai SDK는 user와 model 역할을 사용합니다.
                role = "user" if m["role"] == "user" else "model"
                contents.append(types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=m["content"])]
                ))
            
            # API 호출 (gemini-2.5-flash-lite 모델 사용)
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7,
                )
            )
            
            full_response = response.text
            message_placeholder.markdown(full_response)
            
            # 어시스턴트 답변 세션 저장
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except APIError as e:
            # Gemini API 관련 오류 처리
            error_msg = f"❌ Gemini API 오류가 발생했습니다: {e.message}"
            message_placeholder.markdown(error_msg)
        except Exception as e:
            # 기타 일반 오류 처리
            error_msg = f"⚠️ 예상치 못한 오류가 발생했습니다: {str(e)}"
            message_placeholder.markdown(error_msg)
