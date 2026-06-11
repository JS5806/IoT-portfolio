from mission1_json_parsing import get_seoul_weather

weather = get_seoul_weather()

print(f"""
현재 온도 :  {weather['temp']}
체감 온도 :  {weather['feels_like']}
날씨 설명 :  {weather['description']}
"""
)

temp = weather['temp']
if temp>=30:
    print("더워요 🔥")
elif temp<=10:
    print("추워요 🥶")
else:
    print("적당해요 😊")