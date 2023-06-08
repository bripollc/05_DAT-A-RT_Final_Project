import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title = "DAT(A)RT", page_icon = ":sunglasses:")

st.header("Neural Transfer Style 🧠")

st.write('Neural transfer is a technique in deep learning and computer vision that blends a content image and a style reference image to generate a new output image that combines features of both. The content image provides high-level information and structure, while the style image captures textures, colors and patterns. These features are extracted using a convolutional neural network to achieve that fusion.')



st.write('A convolutional neural network (CNN) is a type of machine learning algorithm used in image processing and visual recognition. It works as follows:')

st.markdown('''
- **Image input**: reception of an image as input composed of pixels, which represent the different colors and structures in the image.
- **Convolution**: application of filters: small matrices on the image that calculate a weighted combination of the pixel values at each position to highlight particular features in the image.
- **Feature maps**: generation of feature maps highlighting the regions where they were detected.
- **Grouping**: pooling operation to the feature maps to reduce dimensionality while preserving key features. 
- **Fully connected layers**: use of fully connected layers to classify extracted features and make predictions. These layers take the input features and process them to generate the final network outputs.
- **Learning and optimization**: adjustment of filter weights and fully connected layers using machine learning techniques. The network is trained by gradually updating the weights to minimize the difference between the network predictions and the actual image labels.
- **Prediction and output**: prediction and classification of new images based on their training.
''')


st.header("My MODEL 🛠️")

st.write('My model uses style neural transfer and convolutional neural networks (CNNs) to fusion a content image (selfie) and a style reference image (chosen from the dataset based on user sentiments) to generate a new image that combines features from both. In my implementation, I use the open source Tensorflow library, together with the Tensorflow Hub extension, which facilitates the use of pre-trained machine learning models. To improve performance and model loading time, I set an environment variable to load the models in compressed format. Specifically, I use the Google Magenta arbitrary image styling model, which specializes in image styling transfer.')

st.markdown('''
- **Tensorflow**: open source library used for machine learning tasks and neural network model development.
- **Tensorflow Hub**: Tensorflow extension that provides pre-trained machine learning models.
- **Environment variable**: used by TensorFlow Hub to compress the format of the models.
- **Google Magenta**: arbitrary image styling model.
''')
