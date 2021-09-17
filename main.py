import cv2
import logging
import numpy as np
from tensorflow import keras
from scipy.misc import imresize
from moviepy.editor import VideoFileClip
logging.basicConfig(level=logging.INFO)

model = keras.models.load_model('models/model.h5')
#print(model)
print([layer.name in layer in model.layers])

class Lanes():
    def __init__(self):
        self.recent_fit = []
        self.avg_fit = []

def road_lines(image):

    small_img = imresize(image, (80, 160, 3))
    small_img = np.array(small_img)
    small_img = small_img[None, :, :, :]

    prediction = model.predict(small_img)[0] * 255

    lanes.recent_fit.append(prediction)

    if len(lanes.recent_fit) > 5:
        lanes.recent_fit = lanes.recent_fit[1:]

    lanes.avg_fit = np.mean(np.array([i for i in lanes.recent_fit]), axis=0)

    # image / matrix
    blanks = np.zeros_like(lanes.avg_fit).astype(np.uint8)
    lane_drawn = np.dstack((blanks, lanes.avg_fit, blanks))

    lane_img = imresize(lane_drawn, (720, 1280, 3))
    result = cv2.addWeighted(image, 1, lane_img, 1, 0)

    return result

if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser()
    parse.add_argument('--input_video', '--i', type=str, default="media/lanes_clip.mp4")
    parse.add_argument('--output_video', '--o', type=str, default="media/lanes_output_clip.mp4")
    args = parse.parse_args()

    # vid_input = VideoFileClip("media/lanes_clip.mp4")
    # vid_output = 'media/lanes_output_clip.mp4'

    vid_input = VideoFileClip(args.input_video)
    logging.info("Video loaded successfully!")
    vid_output = args.output_video

    lanes = Lanes()

    video_clip = vid_input.fl_image(road_lines)
    video_clip.write_videofile(vid_output, audio=False)
    logging.info("Lanes predicted successfully!")
    print(f"Find output video in {vid_output}")
