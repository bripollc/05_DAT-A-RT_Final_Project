import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image

import os
import random

import tensorflow_hub as hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'


# MOVEMENT

def find_closest_movement(df, pos_avg, neu_avg, neg_avg): 
    """
    This function calculates the Euclidean distance between a given 
    vector of values (represented by pos_avg, neu_avg and neg_avg). 
    Then, it finds the index of the minimum distance value and returns 
    the artistic movement corresponding to that index.
    """
    distances = np.sqrt((df['Pos_avg'] - pos_avg) ** 2 +
                        (df['Neu_avg'] - neu_avg) ** 2 +
                        (df['Neg_avg'] - neg_avg) ** 2)
    
    closest_index = distances.idxmin()
    closest_movement = df.loc[closest_index, 'Movement']
    
    return closest_movement



def get_random_movement_path(movement):
    """
    This function takes a "movement" argument, which represents the name of an artistic movement. 
    Then, it uses that name to construct a path to a folder containing images related to that movement
    and returns a random image.
    
    """
    movement_folder = os.path.join("images", "WikiArt", movement)
    files = os.listdir(movement_folder)
    random_image = random.choice(files)
    style_path = os.path.join(movement_folder, random_image)
    return style_path


def load_img(path_to_img):
    """
    This function loads an image and performs a series of transformations. 
    Finally, the function returns the processed and resized image tensor.
    """
    max_dim = 512
    img = tf.io.read_file(path_to_img) # read the image
    img = tf.image.decode_image(img, channels=3) # decode the image
    img = tf.image.convert_image_dtype(img, tf.float32) # normalizes pixel values

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape) # scale the image dimensions
    img = img[tf.newaxis, :] # adds an additional dimension to the image tensor
    
    return img


def stylize_image_movement(content_image, movement_image):
    """
    This function loads a pre-trained image style model from TensorFlow Hub
    and uses it to apply the style of a content image to a motion image.
    It returns the styled image.
    """
    # charge pre-trained image style model
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # stylize the content image with the selected movement
    stylized_image = hub_model(tf.constant(content_image), tf.constant(movement_image))[0]

    return stylized_image



def tensor_to_image_movement(tensor, content_path):
    """
    This function turns a tensor into an image, scaling the values and adjusting 
    the dimensions as necessary to obtain an image suitable for display.
    """
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]

    image = PIL.Image.fromarray(tensor)
    
    path_to_save = f"images/cam_pictures/final_img_movement/final_{content_path.split('/')[-1]}"
    image.save(path_to_save)
    os.system(f"open {path_to_save}")
    return "Done!"





# ARTIST

def find_closest_artist(df, pos_avg, neu_avg, neg_avg):
    """
    This function calculates the Euclidean distance between a given 
    vector of values (represented by pos_avg, neu_avg and neg_avg). 
    Then, it finds the index of the minimum distance value and returns 
    the artist corresponding to that index.
    """
    distances = np.sqrt((df['Pos_avg'] - pos_avg) ** 2 +
                        (df['Neu_avg'] - neu_avg) ** 2 +
                        (df['Neg_avg'] - neg_avg) ** 2)
    
    closest_index = distances.idxmin()
    closest_artist = df.loc[closest_index, 'Artist']
    
    return closest_artist

def get_random_artist_path(df_clean, artist, images_directory):
    artist_df = df_clean[df_clean['Artist'] == artist]  # Filter df_clean by selected artist
    artist_ids = artist_df['ID'].tolist()  # Obtain list of ID's from the artist
    random_id = random.choice(artist_ids)  # Choose a random ID from the list

    # Find the movement corresponding to the selected ID in df_clean
    movement = df_clean[df_clean['ID'] == random_id]['Movement'].values[0]

    image_path = os.path.join(images_directory, 'WikiArt', movement.replace(" ", "_"), random_id + ".jpg")  # Build path using the work ID and the movement.

    return image_path

# recall load_img(path_to_img)

def stylize_image_artist(content_image, artist_image):
    """
    This function loads a pre-trained image style model from TensorFlow Hub
    and uses it to apply the style of a content image to a motion image.
    It returns the styled image.
    """
    # charge pre-trained image style model
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # stylize the content image with the selected movement
    stylized_image = hub_model(tf.constant(content_image), tf.constant(artist_image))[0]

    return stylized_image


def tensor_to_image_artist(tensor, content_path):
    """
    This function turns a tensor into an image, scaling the values and adjusting 
    the dimensions as necessary to obtain an image suitable for display.
    """
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]

    image = PIL.Image.fromarray(tensor)
    
    path_to_save = f"images/cam_pictures/final_img_artist/final_{content_path.split('/')[-1]}"
    image.save(path_to_save)
    os.system(f"open {path_to_save}")
    return "Done!"
