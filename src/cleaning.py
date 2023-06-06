import pandas as pd
import html
import os
import re



def clean_html_text(df):
    """
    This function, applies the html.unescape() function to each row 
    in the'Title' and 'Artist' columns to convert any HTML escape characters 
    in the strings back to their original form.
    """
    df['Title'] = df['Title'].apply(lambda x: html.unescape(x))
    df['Artist'] = df['Artist'].apply(lambda x: html.unescape(x))
    return df


def category_clean(df):
    
    """
    This function is used to clean and update the "Category" column. 
    It modifies some "ambiguous" categories based on specific conditions.
    """
    
    # Neoclassicism,Romanticism
    df.loc[df['Title'] == 'Malvine, Dying in the Arms of Fingal', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'Charlotte Rothsch, Baroness Anselm De Rothschild', 'Category'] = 'Romanticism'
    df.loc[df['Title'] == 'O Milagre de Ourique', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'Mademoiselle Lange as Venus', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'Pygmalion et Galatée', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'Retrato equestre de João V de Portugal', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'The Worship of the Mages', 'Category'] = 'Neoclassicism'
    df.loc[df['Title'] == 'Napoleon I in Coronation robes', 'Category'] = 'Romanticism'

    # Cubism,Expressionism
    df.loc[df['Title'] == 'Harvest', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'Orfeu nos Infernos', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'Portret Van Elizabeth Sergejevna Potehinoj', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'The Street Enters the House', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'Landscape with a sail', 'Category'] = 'Expressionism'
    df.loc[df['Title'] == 'Orfeu nos Infernos (detail)', 'Category'] = 'Cubism'
    df.loc[(df['Title'] == 'Nude') & (df['Artist'] == 'Lajos Tihanyi'), 'Category'] = 'Expressionism'
    df.loc[df['Title'] == 'Yard in Crimea', 'Category'] = 'Expressionism'

    # Abstract Art,Cubism
    df.loc[df['Title'] == 'Composition monumentale', 'Category'] = 'Abstract Art'
    df.loc[df['Title'] == 'Himmel', 'Category'] = 'Abstract Art'
    df.loc[df['Title'] == 'Femme à la blouse jaune', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'Lucky Strike', 'Category'] = 'Abstract Art'
    df.loc[df['Title'] == 'Chess Players III', 'Category'] = 'Cubism'
    df.loc[df['Title'] == 'Composition I (Still life)', 'Category'] = 'Abstract Art'
    df.loc[df['Title'] == 'In the Hold', 'Category'] = 'Abstract Art'

    # Color Field Painting,Lyrical Abstraction
    df.loc[df['Category'] == 'Color Field Painting,Lyrical Abstraction', 'Category'] = 'Color Field Painting'

    # Abstract Art,Surrealism
    df.loc[df['Title'] == 'Hot Air Balloon', 'Category'] = 'Abstract Art'
    df.loc[df['Title'] == 'Modality Series, Spring Awakening 854A', 'Category'] = 'Surrealism'
    df.loc[df['Title'] == 'Dux et Comes I', 'Category'] = 'Abstract Art'

    # Abstract Expressionism,Minimalism
    df.loc[df['Category'] == 'Abstract Expressionism,Minimalism', 'Category'] = 'Abstract Expressionism'

    # Color Field Painting,Minimalism 
    df.loc[df['Title'] == '586/69 (Gerundetes Rot)', 'Category'] = 'Color Field Painting'
    df.loc[(df['Title'] == 'Untitled') & (df['Artist'] == 'Mark Rothko'), 'Category'] = 'Color Field Painting'
    df.loc[df['Title'] == 'The Wild', 'Category'] = 'Minimalism'

    # Art Informel,Magic Realism
    df.loc[df['Category'] == 'Art Informel,Magic Realism', 'Category'] = 'Magic Realism'

    #Abstract Expressionism,Lyrical Abstraction
    df.loc[df['Category'] == 'Abstract Expressionism,Lyrical Abstraction', 'Category'] = 'Lyrical Abstraction'

    # Abstract Expressionism,Color Field Painting
    df.loc[df['Title'] == 'Tanabata', 'Category'] = 'Color Field Painting'
    df.loc[df['Title'] == 'Reefs', 'Category'] = 'Abstract Expressionism'
    
    # 1_element
    df.loc[df['Category'] == 'Neo-Expressionism,Pop Art', 'Category'] = 'Neo-Expressionism'
    df.loc[df['Category'] == 'Magic Realism,Neoclassicism', 'Category'] = 'Magic Realism'
    df.loc[df['Category'] == 'Art Informel,Minimalism', 'Category'] = 'Art Informel'
    df.loc[df['Category'] == 'Abstract Expressionism,Surrealism', 'Category'] = 'Surrealism'
    df.loc[df['Category'] == 'Magic Realism,Surrealism', 'Category'] = 'Surrealism'
    df.loc[df['Category'] == 'Rococo,Romanticism', 'Category'] = 'Romanticism'
    df.loc[df['Category'] == 'Cubism,Post-Impressionism', 'Category'] = 'Cubism'
    df.loc[df['Category'] == 'Expressionism,Post-Impressionism', 'Category'] = 'Expressionism'
    df.loc[df['Category'] == 'Abstract Art,Post-Impressionism', 'Category'] = 'Abstract Art'
    df.loc[df['Category'] == 'Abstract Art,Color Field Painting', 'Category'] = 'Abstract Art'
    df.loc[df['Category'] == 'Impressionism,Post-Impressionism', 'Category'] = 'Post-Impressionism'
    df.loc[df['Category'] == 'Abstract Art,Abstract Expressionism', 'Category'] = 'Abstract Expressionism'
    df.loc[df['Category'] == 'Magic Realism,Neo-Expressionism', 'Category'] = 'Magic Realism'
    df.loc[df['Category'] == 'Cubism,Surrealism', 'Category'] = 'Surrealism'

    df.loc[df['Category'] == 'Northern Renaissance', 'Category'] = 'Northern-Renaissance'
    df.loc[df['Category'] == 'Pop Art', 'Category'] = 'Pop-Art'
    df.loc[df['Category'] == 'Art Informel ', 'Category'] = 'Art-Informel'
    df.loc[df['Category'] == 'Pop Art', 'Category'] = 'Color-Field-Painting'
    df.loc[df['Category'] == 'Art Informel', 'Category'] = 'Art-Informel'
    df.loc[df['Category'] == 'Abstract Art', 'Category'] = 'Abstract-Art'
    df.loc[df['Category'] == 'Abstract Expressionism', 'Category'] = 'Abstract-Expressionism'
    df.loc[df['Category'] == 'Lyrical Abstraction', 'Category'] = 'Lyrical-Abstraction'
    df.loc[df['Category'] == 'Magic Realism', 'Category'] = 'Magic-Realism'
    df.loc[df['Category'] == 'Early Renaissance', 'Category'] = 'Early-Renaissance'
    df.loc[df['Category'] == 'High Renaissance', 'Category'] = 'High-Renaissance'
    
    df.loc[df['Category'] == 'Color Field Painting', 'Category'] = 'Color-Field-Painting'
    return df


def century_clean(df):
    """
    this function performs the cleanup of the values in the "Year" column. 
    It uses a dictionary to map each abbreviated century to a numeric value 
    corresponding to the average between the beginning and the approximate 
    end of the century.
    """
    
    cambios = {
        'XVI cent.': '1550',
        'XV-XVI cent.': '1550',
        'XVII cent.': '1650',
        'XVI-XVII cent.': '1600',
        'XVIII cent.': '1750',
        'XVIII-XIX cent.': '1800',
        'XIX cent.': '1850',
        'XIX-XX cent.': '1950',
        'XVII-XVIII cent.': '1750',
        'XX-XXI cent.': '2000',
        'XV cent.': '1450',
        'XIV-XV cent.': '1350',
        'XX cent.': '1900'
}
    
    df['Year'] = df['Year'].replace(cambios)
    
    return df



def year_clean(cell):
    """
    this function performs a cleanup of the Year column. 
    It converts ranges of years to a single value as the mean rounded up.
    """

    if  "-" in cell:
        try:
            start_year = int(cell.split('-')[0])
            end_year = int(cell.split('-')[1])

            average = (start_year + end_year) // 2 + (start_year + end_year) % 2
            return average
        
        except (ValueError, AttributeError):
            return cell
        
    else:
        return cell
    



def apply_year_clean(df):
    """
    This function applies the year_clean function to the entire df to obtain
    a df with a new column containing the cleaned values of the "Year" column.
    """
    df["Year_2"] = df["Year"].apply(year_clean)
    return df




def rename_reorder_columns(df):
    """
    This function renames and orders the columns of the df.
    """
    new_column_names = {
        'ID': 'ID',
        'Style': 'Style',
        'Category': 'Movement',
        'Artist': 'Artist',
        'Title': 'Title',
        'Year': 'Year',
        'Year_2': 'Year_2',
        'Is painting': 'Painting_Y_N',
        'Face/body': 'Face-body',
        'Ave. art rating': 'Avg_rating',
        'Art (image+title): agreeableness': 'IT_agreeableness',
        'Art (image+title): anger': 'IT_anger',
        'Art (image+title): anticipation': 'IT_anticipation',
        'Art (image+title): arrogance': 'IT_arrogance',
        'Art (image+title): disagreeableness': 'IT_disagreeableness',
        'Art (image+title): disgust': 'IT_disgust',
        'Art (image+title): fear': 'IT_fear',
        'Art (image+title): gratitude': 'IT_gratitude',
        'Art (image+title): happiness': 'IT_happiness',
        'Art (image+title): humility': 'IT_humility',
        'Art (image+title): love': 'IT_love',
        'Art (image+title): optimism': 'IT_optimism',
        'Art (image+title): pessimism': 'IT_pessimism',
        'Art (image+title): regret': 'IT_regret',
        'Art (image+title): sadness': 'IT_sadness',
        'Art (image+title): shame': 'IT_shame',
        'Art (image+title): shyness': 'IT_shyness',
        'Art (image+title): surprise': 'IT_surprise',
        'Art (image+title): trust': 'IT_trust',
        'Art (image+title): neutral': 'IT_neutral',
        'ImageOnly: agreeableness': 'I_agreeableness',
        'ImageOnly: anger': 'I_anger',
        'ImageOnly: anticipation': 'I_anticipation',
        'ImageOnly: arrogance': 'I_arrogance',
        'ImageOnly: disagreeableness': 'I_disagreeableness',
        'ImageOnly: disgust': 'I_disgust',
        'ImageOnly: fear': 'I_fear',
        'ImageOnly: gratitude': 'I_gratitude',
        'ImageOnly: happiness': 'I_happiness',
        'ImageOnly: humility': 'I_humility',
        'ImageOnly: love': 'I_love',
        'ImageOnly: optimism': 'I_optimism',
        'ImageOnly: pessimism': 'I_pessimism',
        'ImageOnly: regret': 'I_regret',
        'ImageOnly: sadness': 'I_sadness',
        'ImageOnly: shame': 'I_shame',
        'ImageOnly: shyness': 'I_shyness',
        'ImageOnly: surprise': 'I_surprise',
        'ImageOnly: trust': 'I_trust',
        'ImageOnly: neutral': 'I_neutral',
        'TitleOnly: agreeableness': 'T_agreeableness',
        'TitleOnly: anger': 'T_anger',
        'TitleOnly: anticipation': 'T_anticipation',
        'TitleOnly: arrogance': 'T_arrogance',
        'TitleOnly: disagreeableness': 'T_disagreeableness',
        'TitleOnly: disgust': 'T_disgust',
        'TitleOnly: fear': 'T_fear',
        'TitleOnly: gratitude': 'T_gratitude',
        'TitleOnly: happiness': 'T_happiness',
        'TitleOnly: humility': 'T_humility',
        'TitleOnly: love': 'T_love',
        'TitleOnly: optimism': 'T_optimism',
        'TitleOnly: pessimism': 'T_pessimism',
        'TitleOnly: regret': 'T_regret',
        'TitleOnly: sadness': 'T_sadness',
        'TitleOnly: shame': 'T_shame',
        'TitleOnly: shyness': 'T_shyness',
        'TitleOnly: surprise': 'T_surprise',
        'TitleOnly: trust': 'T_trust',
        'TitleOnly: neutral': 'T_neutral'
    }

    column_order = [
        'ID',
        'Style',
        'Movement',
        'Artist',
        'Title',
        'Year',
        'Year_2',
        'Painting_Y_N',
        'Face-body',
        'Avg_rating',        
        # Image + Title
            # positive
        'IT_gratitude',
        'IT_happiness',
        'IT_humility',
        'IT_love',
        'IT_optimism',
        'IT_trust',        
            # neutral             
        'IT_agreeableness',
        'IT_anticipation',
        'IT_disagreeableness',
        'IT_shyness',
        'IT_surprise',
        'IT_neutral',
            # negative        
        'IT_anger',
        'IT_arrogance',        
        'IT_disgust',
        'IT_fear',
        'IT_pessimism',
        'IT_regret',
        'IT_sadness',
        'IT_shame',
        
        # Image
            # positive        
        'I_gratitude',
        'I_happiness',
        'I_humility',
        'I_love',
        'I_optimism',
        'I_trust',        
             # neutral                  
        'I_agreeableness',
        'I_anticipation',
        'I_disagreeableness',
        'I_shyness',
        'I_surprise',
        'I_neutral',
            # negative              
        'I_anger',
        'I_arrogance',        
        'I_disgust',
        'I_fear',
        'I_pessimism',
        'I_regret',
        'I_sadness',
        'I_shame',    
        
        # Title
            # positive        
        'T_gratitude',
        'T_happiness',
        'T_humility',
        'T_love',
        'T_optimism',
        'T_trust',        
             # neutral                  
        'T_agreeableness',
        'T_anticipation',
        'T_disagreeableness',
        'T_shyness',
        'T_surprise',
        'T_neutral',
            # negative              
        'T_anger',
        'T_arrogance',        
        'T_disgust',
        'T_fear',
        'T_pessimism',
        'T_regret',
        'T_sadness',
        'T_shame',  
            
    ]

    df = df.rename(columns=new_column_names)
    df = df[column_order]
    return df






# MOVEMENT DF
def movement_averages(df):
    df_avg = df.groupby('Movement').agg({
        'IT_gratitude': 'mean',
        'IT_happiness': 'mean',
        'IT_humility': 'mean',
        'IT_love': 'mean',
        'IT_optimism': 'mean',
        'IT_trust': 'mean',
        'IT_agreeableness': 'mean',
        'IT_anticipation': 'mean',
        'IT_disagreeableness': 'mean',
        'IT_shyness': 'mean',
        'IT_surprise': 'mean',
        'IT_neutral': 'mean',
        'IT_anger': 'mean',
        'IT_arrogance': 'mean',
        'IT_disgust': 'mean',
        'IT_fear': 'mean',
        'IT_pessimism': 'mean',
        'IT_regret': 'mean',
        'IT_sadness': 'mean',
        'IT_shame': 'mean',
    }).reset_index()

    df_avg['Pos_avg'] = df_avg[['IT_gratitude', 'IT_happiness', 'IT_humility', 'IT_love', 'IT_optimism', 'IT_trust']].mean(axis=1).round(3)
    df_avg['Neu_avg'] = df_avg[['IT_agreeableness', 'IT_anticipation', 'IT_disagreeableness', 'IT_shyness', 'IT_surprise', 'IT_neutral']].mean(axis=1).round(3)
    df_avg['Neg_avg'] = df_avg[['IT_anger', 'IT_arrogance', 'IT_disgust', 'IT_fear', 'IT_pessimism', 'IT_regret', 'IT_sadness', 'IT_shame']].mean(axis=1).round(3)

    df = df_avg[['Movement', 'Pos_avg', 'Neu_avg', 'Neg_avg']]
    
    return df



# ARTIST DF
def artist_averages(df):
    df_avg_artist= df.groupby('Artist').agg({
        'IT_gratitude': 'mean',
        'IT_happiness': 'mean',
        'IT_humility': 'mean',
        'IT_love': 'mean',
        'IT_optimism': 'mean',
        'IT_trust': 'mean',

        'IT_agreeableness': 'mean',
        'IT_anticipation': 'mean',
        'IT_disagreeableness': 'mean',
        'IT_shyness': 'mean',
        'IT_surprise': 'mean',
        'IT_neutral': 'mean',

        'IT_anger': 'mean',
        'IT_arrogance': 'mean',
        'IT_disgust': 'mean',
        'IT_fear': 'mean',
        'IT_pessimism': 'mean',
        'IT_regret': 'mean',
        'IT_sadness': 'mean',
        'IT_shame': 'mean',
    }).reset_index()

    df_avg_artist['Pos_avg'] = df_avg_artist[['IT_gratitude', 'IT_happiness', 'IT_humility', 'IT_love', 'IT_optimism', 'IT_trust']].mean(axis=1).round(3)
    df_avg_artist['Neu_avg'] = df_avg_artist[['IT_agreeableness', 'IT_anticipation', 'IT_disagreeableness', 'IT_shyness', 'IT_surprise', 'IT_neutral']].mean(axis=1).round(3)
    df_avg_artist['Neg_avg'] = df_avg_artist[['IT_anger', 'IT_arrogance', 'IT_disgust', 'IT_fear', 'IT_pessimism', 'IT_regret', 'IT_sadness', 'IT_shame']].mean(axis=1).round(3)

    df = df_avg_artist[['Artist', 'Pos_avg', 'Neu_avg', 'Neg_avg']]
    
    return df