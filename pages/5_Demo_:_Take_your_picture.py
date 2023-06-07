import os
import re
import random
import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import PIL.Image
import pandas as pd
import tempfile

os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
#_____________________________________________________

@st.cache(allow_output_mutation=True)
def load_movement_dataframe():
    df = pd.read_csv("data/df_movement.csv")
    return df


def find_closest_movement(df, pos_avg, neu_avg, neg_avg):
    distances = np.sqrt((df['Pos_avg'] - pos_avg) ** 2 +
                        (df['Neu_avg'] - neu_avg) ** 2 +
                        (df['Neg_avg'] - neg_avg) ** 2)
    closest_index = distances.idxmin()
    closest_movement = df.loc[closest_index, 'Movement']
    return closest_movement


def get_random_movement_path(movement):
    movement_folder = os.path.join("images", "WikiArt", movement)
    files = os.listdir(movement_folder)
    random_image = random.choice(files)
    style_path = os.path.join(movement_folder, random_image)
    return style_path


def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim
    new_shape = tf.cast(shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img


def stylize_image_movement(content_image, movement_image):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(content_image, movement_image)[0]
    return stylized_image


def tensor_to_image_movement(tensor, content_path):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    image = PIL.Image.fromarray(tensor)
    path_to_save = f"images/cam_pictures/final_img_movement/final_{content_path.split('/')[-1]}"
    image.save(path_to_save)
    return path_to_save

#_____________________________________________________

@st.cache(allow_output_mutation=True)
def load_artist_dataframe():
    df = pd.read_csv("data/df_artist.csv")
    return df

def find_closest_artist(df, pos_avg, neu_avg, neg_avg):
    distances = np.sqrt((df['Pos_avg'] - pos_avg) ** 2 +
                        (df['Neu_avg'] - neu_avg) ** 2 +
                        (df['Neg_avg'] - neg_avg) ** 2)
    
    closest_index = distances.idxmin()
    closest_artist = df.loc[closest_index, 'Artist']
    
    return closest_artist

def get_random_artist_path(df_clean, artist):
    images_directory = "images/"
    artist_df = df_clean[df_clean['Artist'] == artist]  # Filter df_clean by selected artist
    artist_ids = artist_df['ID'].tolist()  # Obtain list of ID's from the artist
    random_id = random.choice(artist_ids)  # Choose a random ID from the list

    # Find the movement corresponding to the selected ID in df_clean
    movement = df_clean[df_clean['ID'] == random_id]['Movement'].values[0]

    style_path = os.path.join(images_directory, 'WikiArt', movement.replace(" ", "_"), random_id + ".jpg")  # Build path using the work ID and the movement.

    return style_path

def stylize_image_artist(content_image, artist_image):
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    stylized_image = hub_model(content_image, artist_image)[0]
    return stylized_image


def tensor_to_image_artist(tensor, content_path):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    image = PIL.Image.fromarray(tensor)
    path_to_save = f"images/cam_pictures/final_img_artist/final_{content_path.split('/')[-1]}"
    image.save(path_to_save)
    return path_to_save


#_____________________________________________________




def main():
    st.title("Let's try it!")
    st.header("#1 Take your best selfie 📸")

    img_file_buffer = st.camera_input("Say cheese!")

    if img_file_buffer is not None:
        img = PIL.Image.open(img_file_buffer)
        
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_img:
            img.save(temp_img.name)
            content_image = load_img(temp_img.name)
        
        st.header("#2 How do you feel today? 🫥")
        pos_sentiment = st.slider('Positive 🙂', -1.0, 1.0, 0.0)
        neu_sentiment = st.slider('Neutral 😶', -1.0, 1.0, 0.0)
        neg_sentiment = st.slider('Negative 🙁', -1.0, 1.0, 0.0)

        st.header("#3 Choose a movement or artist 👩🏻‍🎨")
        if st.button("Movement"):
            df_mov = load_movement_dataframe()
            movement_name = find_closest_movement(df_mov, pos_sentiment, neu_sentiment, neg_sentiment)
            movement_path = get_random_movement_path(movement_name)
            movement_image = load_img(movement_path)
            stylized_movement_img = stylize_image_movement(content_image, movement_image)
            ntl_movement_img = tensor_to_image_movement(stylized_movement_img, movement_path)
            st.image(ntl_movement_img, use_column_width=True)

            df_clean = pd.read_csv("data/WikiArt-Emotions-Clean.csv")

        
            col1, col2 = st.columns(2)

            # Mostrar la imagen generada en la primera columna
            with col1:
                original_image = PIL.Image.open(movement_path)
                st.subheader("Movement Image")
                st.image(original_image, caption="Selected Movement Image", use_column_width=True)

                # Obtener el ID de la imagen seleccionada
                image_id = movement_path.split('/')[-1].split('.')[0]

                # Buscar la información correspondiente en df_clean
                image_info = df_clean[df_clean['ID'] == image_id]
                artist = image_info['Artist'].values[0]
                movement = image_info['Movement'].values[0]
                title = image_info['Title'].values[0]
                year = image_info['Year'].values[0]
            with col2:
                # Mostrar la información en la segunda columna
                st.subheader("Information")
                st.write(f"Artist: {artist}")
                st.write(f"**Movement: {movement}**")
                st.write(f"Title: {title}")
                st.write(f"Year: {year}")



        if st.button("Artist"):
            df_clean = pd.read_csv("data/WikiArt-Emotions-Clean.csv")
            df_artist = load_artist_dataframe()
            artist_name = find_closest_artist(df_artist, pos_sentiment, neu_sentiment, neg_sentiment)
            artist_path = get_random_artist_path(df_clean, artist_name)
            artist_image = load_img(artist_path)
            stylized_artist_img = stylize_image_artist(content_image, artist_image)
            ntl_artist_img = tensor_to_image_artist(stylized_artist_img, artist_path)
            st.image(ntl_artist_img, use_column_width=True)


            col1, col2 = st.columns(2)

            # Mostrar la imagen generada en la primera columna
            with col1:
                original_image = PIL.Image.open(artist_path)
                st.subheader("Selected image")
                st.image(original_image, caption="Artist that best defines you today", use_column_width=True)

            with col2:
                # Mostrar la información en la segunda columna
                st.subheader("Information")
                # Obtener el ID de la imagen seleccionada
                image_id = artist_path.split('/')[-1].split('.')[0]
                # Buscar la información correspondiente en df_clean
                image_info = df_clean[df_clean['ID'] == image_id]
                artist = image_info['Artist'].values[0]
                movement = image_info['Movement'].values[0]
                title = image_info['Title'].values[0]
                year = image_info['Year'].values[0]

                st.write(f"Artist: {artist}")
                st.write(f"Movement: {movement}")
                st.write(f"Title: {title}")
                st.write(f"Year: {year}")




if __name__ == "__main__":
    main()
