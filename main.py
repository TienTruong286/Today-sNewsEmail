import requests
from send import send_email


api_key = API_KEY
url = "https://newsdata.io/api/1/news?apikey=APIKEY&q=tesla&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["results"][:20]:
    if article["title"] is not None:
        body ="Subject: Today's news" + "\n" + body + article["title"] + "\n" +article["description"] +"\n"+  article['link'] + "\n"

body = body.encode("utf-8")
send_email(message = body)


