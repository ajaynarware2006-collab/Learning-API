import requests as rq

response=rq.get("https://randomuser.me/api?results=5")

if response.status_code == 200:

    data=response.json()
    if not data["results"]:
        print("User Not Found")
    
    else:
        for index,user in enumerate(data["results"],1):

            location=user["location"]

            first=user["name"]["first"]
            last=user["name"]["last"]
            email=user["email"]
            country=location["country"]
            age=user["dob"]["age"]
            phone_no=user["phone"]
            user_name=user["login"]["username"]
            timezone=location["timezone"]["offset"]

            print(f"user {index}")
            print("=========================================")
            print(f"Name      : {first} {last}")
            print(f"Age       : {age}")
            print(f"Email     : {email}")
            print(f"Phone no. : {phone_no}")
            print(f"Country   : {country}")
            print(f"Timezone  : {timezone}")
            print(f"Usernsme  : {user_name}")
            print("=========================================")

else:
    print("Request fail")
