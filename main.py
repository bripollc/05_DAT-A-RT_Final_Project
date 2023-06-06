import src.cleaning as clean
import src.take_your_picture as camera
import src.neural_transfer_style as nts


import os
import pandas as pd

#----------------------------------------------------------------------------
# 0. CHARGE ORIGINAL DataFrame
    # The WikiArt Emotions Dataset
    # Saif M. Mohammad (saif.mohammad@nrc-cnrc.gc.ca) 
    # http://saifmohammad.com/WebPages/wikiartemotions.html

#file_path = "05_final_project/data/WikiArt-Emotions/WikiArt-Emotions-All.tsv"

df = pd.read_csv("data/WikiArt-Emotions/WikiArt-Emotions-All.tsv", sep='\t')

#----------------------------------------------------------------------------

# 01. CLEANING
    # clean original df
df_clean = clean.clean_html_text(df)
df_clean = clean.category_clean(df_clean)
df_clean = clean.century_clean(df_clean)
df_clean = clean.apply_year_clean(df_clean)
df_clean = clean.rename_reorder_columns(df_clean)
#print (df_clean.head(5))

#df_clean.to_csv("/data/WikiArt-Emotions/WikiArt-Clean.csv") # save



    # movement df
df_movement = clean.movement_averages(df_clean)
#df_movement.to_csv("/data/WikiArt-Movement.csv") # save
#print (df_movement.head(5))
    # artist df
df_artist = clean.artist_averages(df_clean)
#df_artist.to_csv("/data/WikiArt-Artist.csv") # save
#print (df_artist.head(5))

#----------------------------------------------------------------------------

# 02. TAKE A PICTURE (open CV)
output_directory = "images/cam_pictures"
content_path = camera.capture_images_from_camera(output_directory)
content_image = nts.load_img(content_path)
#print(content_path)
#----------------------------------------------------------------------------

# 03. NEURAL TRANSFER STYLE

    # (1) MOVEMENT
pos_avg = 0.091
neu_avg = 0.010
neg_avg = 0.070

movement_name = nts.find_closest_movement(df_movement, pos_avg, neu_avg, neg_avg)
movement_path = nts.get_random_movement_path(movement_name)
print(movement_name)
print(movement_path)
movement_image = nts.load_img(movement_path)

#print(content_image)
#print(movement_image)

stylized_movement_img = nts.stylize_image_movement(content_image, movement_image)
ntl_movement_img = nts.tensor_to_image_movement(stylized_movement_img, content_path)
#print(ntl_movement_img)
"""
    # (2) ARTIST
images_directory = "images/"

pos_avg_2 = 0.080
neu_avg_2 = 0.054
neg_avg_2 = 0.142

artist_name = nts.find_closest_artist(df_artist, pos_avg_2, neu_avg_2, neg_avg_2) 
artist_path = nts.get_random_artist_path(df_clean, artist_name, images_directory)
#print(artist_name)
print(artist_path)

#content_image = nts.load_img(content_path)
artist_image = nts.load_img(artist_path)
#print(artist_image)

stylized_artist_img = nts.stylize_image_artist(content_image, artist_image)
ntl_artist_img = nts.tensor_to_image_artist(stylized_artist_img, content_path)
"""