from firebase import firebase

firebase = firebase.FirebaseApplication('https://vigil-15d90.firebaseio.com/', None)

result = firebase.get('/users', '')
for i in result.keys():
    print(result[i]['fcm_token'])
