from flask import Flask,render_template,request,url_for,redirect,jsonify
import requests, json
from firebase import firebase
from demo import run_demo
import pyrebase
from db_web import db_web
import time
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://vigil-15d90.firebaseio.com/', None)

@app.route('/')
def index():
    return render_template("/home.html")


@app.route('/test', methods=['POST'])
def index1():  
    
    #temp = run_demo()
    #time.sleep(50)
    #temp = temp+10
    
    ttl = "Says"
    msg = "Important"
    lat = 13.054500
    lon = 77.545590
    action = request.form['action']
    print(action)
    l = []
    result = firebase.get('/users', '')
    for i in result.keys():
        token = result[i]['fcm_token']
        url = 'https://fcm.googleapis.com/fcm/send'
        server_key = 'AAAA1RvIP5g:APA91bHUm4jiUYPhPaFRS_j7tR1qJDgZdgvvG-brzRyT_uOuCVxHm48OLREuE_RbACIYufbNdceb9bth_mFVJZrOctLuw4NMHBeCZ1Dzqh3X78CeSDQUtVRkNVtpqi9lVrNwajYTfloq'
        myobj = {'to':token,'notification':{'title':ttl, 'body':msg, 'click_action':action}, 'data':{'lat':lat, 'lon':lon}}
       
        r = requests.post(url, json = myobj, headers = {'Authorization':'key='+server_key, 'Content-Type' : 'application/json'})
        print(r)


    #time.sleep(25)
    db_web()
    return render_template("/test.html")

if __name__ == "__main__":
    app.run(debug=True)