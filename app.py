from flask import Flask,render_template,request,session,jsonify
from textblob import TextBlob
from dataclasses import dataclass
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emoji',methods=['POST'])
def emoji():
    q=request.get_json()
    result=q['value']
    print(result)
    threshold=0.5
    sentiment = TextBlob(result).sentiment.polarity
    friendly_threshold = threshold
    hostile_threshold = -threshold
    if sentiment >= friendly_threshold:
        ans={'emoji':'😊','sentiment':sentiment,'message':result} 
    elif sentiment <= hostile_threshold:
        ans={'emoji':'😡','sentiment':sentiment,'message':result}
    else:
        ans={'emoji':'😐','sentiment':sentiment,'message':result}
    return jsonify(result=ans)
if __name__ == '__main__':
    app.run(debug=True)