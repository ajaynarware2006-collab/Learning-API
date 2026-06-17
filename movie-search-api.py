import requests as rq

movie_name=input("Enter movie name : ")
response=rq.get(f"http://www.omdbapi.com/?t={movie_name}&apikey=12ed4676")
if response.status_code==200:
    data=response.json()

    if data["Response"] != "True":
        print("Movie not found")

    
    else:
        title=data["Title"]
        year=data["Year"]
        genre=data["Genre"]
        rating=data["imdbRating"]
        released=data["Released"]

        print("===================================")
        print(f"Title       : {title}")
        print(f"Genre       : {genre}")
        print(f"IMDB Rating : {rating}")
        print(f"Released    : {released}")
        print(f"====================================")
    

else:
    print(f"you get {response.status_code} error")