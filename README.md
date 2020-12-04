# dataset-done

### installations

#### pip
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
```
#### OpenCV
```$ pip install opencv-contrib-python```
#### Python labraries
```$ pip install scipy matplotlib pillow```
#### Tensorflow and Keras

```
$ pip install tensorflow
$ pip install keras
```

### Run
#### extract-images-from-video
Extracts every frame by default from a video and saves the extracted images in a folder.

```python extract-images-from-video.py --video_path [video_path]```

You want to assign nth number so that you can take ever nth frame from a video.

```python extract-images-from-video.py --video_path [video_path] --n_frames [integer number]```

For examples

```python extract-images-from-video.py --video_path my_videos --n_frames 20```