from flask import Flask
import requests
import pprint
app= Flask(__name__)

pp =pprint.PrettyPrinter(indent=3)
url = "https://youtube138.p.rapidapi.com/channel/videos/"

querystring = {"id":"UCJ5v_MCY6GNUBTO8-D3XoAg","hl":"en","gl":"US"}

headers = {
	"X-RapidAPI-Key": "9230f7261amsh1fb87bc69960675p13ef06jsnefe248b2e69a",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pp.pprint(response.json())
@app.route('/')
def index():
    return "Hello World"

if(__name__)=="__main__":
    app.run(debug=True)