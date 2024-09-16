# profile_face_detection
To detect faces using OpenCV, you typically use the Haar Cascade Classifier, which is a machine learning object detection method used to identify objects in images or videos. Here's a step-by-step guide for face detection using OpenCV in Python:

1. Install OpenCV:
If you haven't installed OpenCV yet, you can do so using pip:

``pip install opencv-python``

2. Load the Pre-trained Haar Cascade Classifier:
OpenCV comes with several pre-trained models, and one of them is for face detection. You can download the Haar Cascade XML file for face detection from OpenCV's GitHub repo, or you can use the one that comes with the library.

The file you’ll need is called ``haarcascade_frontalface_default.xml``, which can be found in the ``opencv/data/haarcascades/`` folder if you have OpenCV installed.


**Detected image**
![detected image](https://github.com/codewithamirshakya/profile_face_detection/blob/main/detect1.png)
![detected image](https://github.com/codewithamirshakya/profile_face_detection/blob/main/detect2.png)
