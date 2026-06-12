"""
Mission1-1. 아래 미션에서 작성한 코드를 외부파일에서 불러와서 현재 온도, 체감 온도, 날씨 설명을 다시 출력하고,
현재 온도에 따른 날씨 표현을 출력하여라.
_______________________
[미션 조건]
30도 이상 → "더워요 🔥
10도 이하 → "추워요 🥶
그 사이   → "적당해요 😊
_____________________________________________________
    | Mission1. 아래 세 가지를 출력하는 코드 완성하기
    | _______________________________________________
    | 현재 온도: XX°C
    | 체감온도: XX°C  
    | 날씨 설명: Sunny / Cloudy / ... (영어로 나와도 됨)
    | _______________________________________________
    | [미션 조건]
    | - requests로 wttr.in API 호출
    | - JSON 파싱해서 원하는 값 추출
    | - get_seoul_weather() 함수로 묶어서 반환
    | - 다른 파일에서 import해서 쓸 수 있는 구조로 만들기
_____________________________________________________
"""

from mission1_json_parsing import now_seoul_weather

weather = now_seoul_weather()

print("현재 온도 : ",weather['temp'])
print("체감 온도 : ",weather['feels_like'])
print("날씨 설명 : ",weather['desc'])

temp = weather['temp']
if temp>=30:
    print("더워요 🔥")
elif temp<=10:
    print("추워요 🥶")
else:
    print("적당해요 😊")