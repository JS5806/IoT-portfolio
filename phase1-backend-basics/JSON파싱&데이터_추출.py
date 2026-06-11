"""
Mission1. 아래 세 가지를 출력하는 코드 완성하기
_______________________________________________
현재 온도: XX°C
체감온도: XX°C  
날씨 설명: Sunny / Cloudy / ... (영어로 나와도 됨)
_______________________________________________
[미션 조건]
  - requests로 wttr.in API 호출
  - JSON 파싱해서 원하는 값 추출
  - get_seoul_weather() 함수로 묶어서 반환
  - 다른 파일에서 import해서 쓸 수 있는 구조로 만들기
"""

##################################### [A1] #####################################
import requests

def get_seoul_weather():
    response = requests.get("https://wttr.in/Seoul?format=j1")  # 설명1
    data = response.json()                                       # 설명1
    current = data['current_condition'][0]                       # 설명1

    return {
        "temp":        int(current['temp_C']),           # 설명3
        "feels_like":  int(current['FeelsLikeC']),       # 설명3
        "description": current['weatherDesc'][0]['value']
    }

if __name__ == "__main__":   # 설명4
    weather = get_seoul_weather()
    print("현재 온도: ", weather['temp'])
    print("체감온도: ", weather['feels_like'])
    print("날씨 설명: ", weather['description'])

################################################################################


"""
[ 코드 리뷰 ]

  ###################### 설명1 - API 호출 패턴 - 암기하기!! ######################
    response = requests.get(URL)      # API 호출
    data = response.json()            # JSON → 딕셔너리 변환
    값 = data['키'][인덱스]['키']      # 원하는 값 파고들기

  ###################### 설명2 - 딕셔너리 3대 메서드 ############################
    data.keys()   → 키 목록 확인 (안에 뭐가 있지?)
    data.values() → 값 목록 확인
    data.items()  → 키+값 쌍 (for 루프에서 자주 씀)

  ###################### 설명3 - API 숫자값 변환 - 암기하기!! ###################
    API에서 뽑은 숫자는 항상 문자열(string)이에요.
    비교/계산 전에 int() 또는 float()로 변환하는 것이 습관이에요.
    예) int(current['temp_C'])  /  float(current['temp_C'])

  ###################### 설명4 - if __name__ == "__main__" - 암기하기!! #########
    이 파일을 직접 실행할 때만 아래 코드가 동작해요.
    다른 파일에서 import 해서 쓸 때는 이 블록이 실행되지 않아요.
    → 함수만 가져다 쓰고 싶을 때 필수 패턴이에요.

  ###################### [디버깅 습관] - 암기하기!! #############################
    response = requests.get("...")
    print(response.status_code)   # 200인지 먼저 확인
    print(response.text[:200])    # 응답 내용 앞부분 확인
    data = response.json()        # 에러나면 위 두 줄이 힌트
  ###############################################################################
"""