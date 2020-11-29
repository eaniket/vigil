import os
from c3d import *
from classifier import *
from utils.visualization_util import *
import pyrebase

def run_demo():

    video_name = os.path.basename(cfg.sample_video_path).split('.')[0]
    print(video_name)
    # read video
    video_clips, num_frames = get_video_clips(cfg.sample_video_path)

    print("Number of clips in the video : ", len(video_clips))

    # build models
    feature_extractor = c3d_feature_extractor()
    classifier_model = build_classifier_model()

    print("Models initialized")

    # extract features
    rgb_features = []
    for i, clip in enumerate(video_clips):
        clip = np.array(clip)
        if len(clip) < params.frame_count:
            continue

        clip = preprocess_input(clip)
        rgb_feature = feature_extractor.predict(clip)[0]
        rgb_features.append(rgb_feature)

        print("Processed clip : ", i)

    rgb_features = np.array(rgb_features)

    print("Shape of rgb_features: ",rgb_features.shape)
    #print(rgb_features)
    # bag features
    rgb_feature_bag = interpolate(rgb_features, params.features_per_bag)

    # classify using the trained classifier model
    predictions = classifier_model.predict(rgb_feature_bag)

    predictions = np.array(predictions).squeeze()

    predictions = extrapolate(predictions, num_frames)

    save_path = os.path.join(cfg.output_folder,  'out.gif')
    # visualize predictions
    x = visualize_predictions(cfg.sample_video_path, predictions, save_path)

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
    print("saving gif")
    path_local = "./output/out.gif" #image path on your system
    path_cloud = "images/foo.jpg" #path on cloud
    storage.child(path_cloud).put(path_local)

    return 1

if __name__ == '__main__':
    run_demo()