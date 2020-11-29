import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils.video_util import *


def visualize_clip(clip, convert_bgr=False, save_gif=False, file_path=None):
    num_frames = len(clip)
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    def update(i):
        if convert_bgr:
            frame = cv2.cvtColor(clip[i], cv2.COLOR_BGR2RGB)
        else:
            frame = clip[i]
        plt.imshow(frame)
        return plt

    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 20ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(0, num_frames), interval=1)
    if save_gif:
        anim.save(file_path, dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()

lis = list()
def visualize_predictions(video_path, predictions, save_path):
    frames = get_video_frames(video_path)
    assert len(frames) == len(predictions)

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.set_tight_layout(True)

    fig_frame = plt.subplot(2, 1, 1)
    fig_frame.set(xlabel="",ylabel="Monitored Video")
    fig_prediction = plt.subplot(2, 1, 2)
    fig_prediction.set_xlim(0, len(frames))
    fig_prediction.set_ylim(0, 1.15)
    fig_prediction.set(xlabel="Frame Number", ylabel="Anomaly Score")

    def update(i):
        frame = frames[i]
        x = range(0, i)
        y = predictions[0:i]
        fig_prediction.plot(x, y, '-')

        #dic[y]=i;

        fig_frame.imshow(frame)
        return plt

# FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 20ms between frames.
    for i in range(1,len(frames)):
        a=predictions[i-1]
        b=predictions[i]
        t = (b-a)
        if t>0.05:
            lis.append(i)

    # print(lis)
    if len(lis)<5:
        print("No anomaly")
    else:
        j=0
        for i in lis:
            print("Anomaly in frame no: ",i)
            # print(type(frames[i]))
            plt.imsave("./output/fr"+str(j)+".png",arr=frames[i])
            j=j+1
    
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(frames), 10), interval=1, repeat=False)

    if save_path:
        anim.save(save_path, dpi=200, writer='imagemagick')
    else:
        plt.show()

    return 11


