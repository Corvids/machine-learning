# Machine Learning Engineer Nanodegree
# Deep Learning
## Project: Build a Digit Recognition Program

### Description

In this project, you will use what you've learned about deep neural networks and convolutional neural networks to create a live camera application or program that prints numbers it observes in real time from images it is given. First, you will design and test a model architecture that can identify sequences of digits in an image. Next, you will train that model so it can decode sequences of digits from natural images by using the Street View House Numbers (SVHN) dataset. After the model is properly trained, you will then test your model using a live camera application (optional) or program on newly-captured images. Finally, once you obtain meaningful results, you will refine your implementation to also localize where numbers are on the image, and test this localization on newly-captured images.

### Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [SciPy](https://www.scipy.org/)
- [scikit-learn](http://scikit-learn.org/0.17/install.html) (v0.17)
- [TensorFlow](http://tensorflow.org)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html).

In addition to the above, for those optionally seeking to use image processing software, you may need one of the following:
- [PyGame](http://pygame.org/)
   - Helpful links for installing PyGame:
   - [Getting Started](https://www.pygame.org/wiki/GettingStarted)
   - [PyGame Information](http://www.pygame.org/wiki/info)
   - [Google Group](https://groups.google.com/forum/#!forum/pygame-mirror-on-google-groups)
   - [PyGame subreddit](https://www.reddit.com/r/pygame/)
- [OpenCV](http://opencv.org/)

For those optionally seeking to deploy an Android application:
- Android SDK & NDK (see this [README](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/android/README.md))

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. Make sure that you select the Python 2.7 installer and not the Python 3.x installer. `pygame` and `OpenCV` can then be installed using one of the following commands:

Mac:  
```bash
conda install -c https://conda.anaconda.org/quasiben pygame
conda install -c menpo opencv=2.4.11
```

Windows & Linux:  
```bash
conda install -c https://conda.anaconda.org/tlatorre pygame
conda install -c menpo opencv=2.4.11
```

### Code

A template notebook is provided as `digit_recognition.ipynb`. While no code is included in the notebook, you will be required to use the notebook to implement the basic functionality of your project and answer questions about your implementation and results.

### Run

In a terminal or command window, navigate to the top-level project directory `digit_recognition/` (that contains this README) and run one of the following commands:

```bash
ipython notebook digit_recognition.ipynb
```  
or
```bash
jupyter notebook digit_recognition.ipynb
```

This will open the Jupyter Notebook software and notebook file in your browser.


### Data

While no data is directly provided with the project, you will be required to download and use the [Street View House Numbers (SVHN) dataset](http://ufldl.stanford.edu/housenumbers/), along with either the [notMNIST](http://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html) or [MNIST](http://yann.lecun.com/exdb/mnist/) datasets. If you've completed the course material, the **notMINIST** dataset should already be available.
