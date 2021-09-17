# Lane detection w/ Semnatic Segmentation

The goal of this project is to perform semantic segmentation on images to label pixels of a road using a 
Fully Convolutional Network. Semantic segmentation is the task of finding what's in an image at the pixel level. 
It can be used by autonomous cars for scene understanding. For example, infering the drivable surfaces in an image 
(road) or objects to avoid (other vehicles, pedestrians) at a fine resolution.

**Install requirements:**

`pip install -r requirements.txt`

or 

`conda env create -f environment.yml`

**Demo:**

`python main.py --i 'media/lane_video.mp4' --o 'media/lane_output_video.mp4'`

**Run:**

`python main.py --i 'path/to/input/video.mp4' --o 'path/to/store/output/video.mp4'`
