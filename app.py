from flask import Flask,render_template
import requests
from numerize.numerize import numerize
import pprint
app= Flask(__name__)

# pp =pprint.PrettyPrinter(indent=3)

# pp.pprint(response.json())
RANDOM_CHANNEL_NAMES =[
'Trendy Trends',
'Anywhere',
'Gen Z Nation',
'Rambling Pen',
'Super',
'Makeupyours',
'Beachy Bird',
'Its Personal',
'Brokers',
'Word On The Street',
'The Factor',
'Moore House',
'Top Dog',
'Efficient Way',
'Neat People',
'The Positive Peach',
'Funfun',
'VidPlex',
'Gap Ideas',
'Watch And Rewatch',
'Collection',
'Channel Calls',
'Urban King',
'Peak',
'Prism',
'Flax',
'Nostalgia']
@app.route('/')
def index():
    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    querystring = {"id":"UCJ5v_MCY6GNUBTO8-D3XoAg","hl":"en","gl":"US"}

    headers = {
	"X-RapidAPI-Key": "9230f7261amsh1fb87bc69960675p13ef06jsnefe248b2e69a",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data =response.json()
    contents= data['contents']
    videos= [video['video'] for video in contents if video['video']['publishedTimeText']]
    
    # return jsonify(videos) #--> import Jsonify in flask
    return render_template('index.html', videos=videos)

@app.template_filter()
def numberize(views):
  return numerize(views, 1)

@app.template_filter()
def highest_quality_image(images):
  return images[3]['url'] if len(images) >= 4 else images[0]['url']
  

if(__name__)=="__main__":
    app.run(debug=True)