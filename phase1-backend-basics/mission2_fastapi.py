"""
Mission2. 아래 조건을 만족하는 FastAPI 서버를 만들어라.
_______________________________________________
실행 후 브라우저에서 http://127.0.0.1:8000/weather 접속하면
현재 서울 날씨 정보가 JSON으로 응답되어야 한다.

예상 응답:
{
    "temp": 27,
    "feels_like": 29,
    "description": "Sunny"
}
_______________________________________________
[미션 조건]
  - FastAPI 앱 인스턴스 생성
  - GET /weather 엔드포인트 만들기
  - mission1_json_parsing.py의 now_seoul_weather() import해서 활용
  - uvicorn으로 실행 후 /weather 응답 확인
_______________________________________________
"""

##################################### [A2] #####################################

from fastapi import FastAPI
from mission1_json_parsing import now_seoul_weather

app = FastAPI()

@app.get("/weather")
def seoul_weather():
    seoul_weather = now_seoul_weather()
    return {
        "temp": seoul_weather['temp'],
        "feels_like": seoul_weather['feels_like'],
        "desc": seoul_weather['desc']
    }

################################################################################


"""
[ 코드 리뷰 ]

  ###################### 설명1 - FastAPI 기본 구조 - 암기하기!! ##################
      | from fastapi import FastAPI
      | 
      | app = FastAPI()           # 서버 인스턴스 생성 (항상 app 이라는 이름 씀)
      | 
      | @app.get("/경로")         # 데코레이터: GET /경로 요청을 이 함수에 연결
      | def 함수명():
      |     return {"키": "값"}   # 딕셔너리 반환 → 자동으로 JSON 변환

  ###################### 설명2 - 실행 방법 - 암기하기!! #########################
    uvicorn 파일명:app --reload
      - 파일명 : .py 제외한 파일 이름
      - app    : FastAPI() 인스턴스 변수명
      - --reload : 코드 수정 시 서버 자동 재시작 (개발용)

  ###################### 설명3 - API 호출 위치 주의!! ###########################
    # ❌ 잘못된 방식 - 서버 시작 시 한 번만 호출 > 값이 고정됨
      | weather = now_seoul_weather()
      |
      | @app.get("/weather")
      | def seoul_weather():
      |     return weather        # 항상 같은 값 반환

    # ✅ 올바른 방식 - 요청마다 함수 안에서 호출 > 항상 최신값
      | @app.get("/weather")
      | def seoul_weather():
      |     weather = now_seoul_weather()   # 요청할 때마다 새로 가져옴
      |     return weather

  ###################### 설명4 - 자동 문서 확인 ##################################
    서버 실행 후 브라우저에서 접속:
    http://127.0.0.1:8000/docs   > Swagger UI (엔드포인트 테스트 가능)
    http://127.0.0.1:8000/redoc  > ReDoc (읽기 전용 문서)

"""
