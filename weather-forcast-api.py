import requests as rq

city=input("Enter city : ")
response=rq.get(f"https://api.weatherapi.com/v1/current.json?key=2103368b2daf4728b3a134449261306&q={city}")
if response.status_code==200:
    data=response.json()
    
    current=data["current"]
    temp_c=current["temp_c"]
    weather_condition=current["condition"]["text"]
    humidity=current["humidity"]

    print("===================================")
    print(f"City        : {city}")
    print(f"Temperature : {temp_c}")
    print(f"Condition   : {weather_condition}")
    print(f"Humidity    : {humidity}%")
    print("===================================")

else:
    print(f"We get {response.status_code} Error")