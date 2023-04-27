# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:09:09 2023
@author: Nehaal
"""

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def get_predict():
    vectoriser = pickle.load(open('vectoriser.pickle', 'rb'))
    model = pickle.load(open('Sentiment-LR.pickle', 'rb'))

    name = request.form['name']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']

    # Predict emotions
    emotions = []
    for inputs in [q1, q2, q3]:
        X = vectoriser.transform([inputs])
        y_pred = model.predict(X)[0]
        emotions.append(y_pred)
            
    occurrences = {}
    for emotion in emotions:
        if emotion in occurrences:
            occurrences[emotion] += 1
        else:
            occurrences[emotion] = 1

    # Find the value with the maximum occurrence
    max_value = max(occurrences, key=occurrences.get)
    major_emotion = max_value
    
    if major_emotion == 1:
        video_id = 'dQw4w9WgXcQ'
        suggestion = 'You seem happy! Check out this funny video.'
    elif major_emotion == 0:
    	video_id = 'LjF9IqvXDjY'
    	suggestion = 'You seem sad. This heartwarming video might make you feel better.'
    else:
    	video_id = 'kTJczUoc26U'
    	suggestion = 'Seems like you are feeling neutral. Check out this interesting video.'

    
    return render_template('result.html', suggestion=suggestion, video_id=video_id)


if __name__ == '__main__':
    app.run(debug=True)
