from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'yly2HmnuZ4mvqPLldocpHi0sE'
consumer_secret = 'YdisDvDj6HLcEknE5ZXqHwO7ZncYrE0u104vqULwuSJbY0dZKr'

access_token = '1101972778570248192-0wVfY2Zv5ZJNTMvIK28cR8MAuJuPHs'
access_token_secret = 'SoYqTQBaxwJZ0LLhZ8cv7iY6elbx046KHagcN1mrsQI8J'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()