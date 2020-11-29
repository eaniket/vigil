import pyrebase

# config = {
#     "apiKey": "AIzaSyCKc3EmsQUim9LQc29C0JiTPGj1ErvQY6I",
#     "authDomain": "vigil-15d90.firebaseapp.com",
#     "databaseURL": "https://vigil-15d90.firebaseio.com",
#     "projectId": "vigil-15d90",
#     "storageBucket": "vigil-15d90.appspot.com",
#     "messagingSenderId": "915294142360",
#     "appId": "1:915294142360:web:15e16c76f439bf885e35ed"
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()
# path_local = "./output/out.gif" #image path on your system
# path_cloud = "images/foo.jpg" #path on cloud
# storage.child(path_cloud).put(path_local)

# path_local = "./output/fr1.png" #image path on your system
# path_cloud = "images/bar.jpg" #path on cloud
# storage.child(path_cloud).put(path_local)

# path_local = "./output/fr2.png" #image path on your system
# path_cloud = "images/foobar.jpg" #path on cloud
# storage.child(path_cloud).put(path_local)
# # r = storage.child(path_cloud).get_url(None)
# # print(r)

def db_web():
    config = {
        "apiKey": "AIzaSyCKc3EmsQUim9LQc29C0JiTPGj1ErvQY6I",
        "authDomain": "vigil-15d90.firebaseapp.com",
        "databaseURL": "https://vigil-15d90.firebaseio.com",
        "projectId": "vigil-15d90",
        "storageBucket": "vigil-15d90.appspot.com",
        "messagingSenderId": "915294142360",
        "appId": "1:915294142360:web:15e16c76f439bf885e35ed"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # path_local = "./output/out.gif" #image path on your system
    # path_cloud = "images/foo.gif" #path on cloud
    # storage.child(path_cloud).put(path_local)

    path_local = "./output/fr1.png" #image path on your system
    path_cloud = "images/bar.jpg" #path on cloud
    storage.child(path_cloud).put(path_local)

    path_local = "./output/fr2.png" #image path on your system
    path_cloud = "images/foobar.jpg" #path on cloud
    storage.child(path_cloud).put(path_local)
    # r = storage.child(path_cloud).get_url(None)
    # print(r)