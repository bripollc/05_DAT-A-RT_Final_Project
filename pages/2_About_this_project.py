import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components


st.title("Dat(A)rt")
st.markdown("The project that...")


st.header("Introduction")
st.write(
    "<div style='font-size:1.2rem'>"
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mi elit, varius vel dapibus eget, facilisis sit amet nisl. Mauris nec tristique eros. Etiam molestie mauris a urna gravida, et molestie justo dignissim. Praesent id quam id eros dignissim ultricies. Pellentesque rhoncus odio quis diam dictum mollis. Vivamus ac eleifend lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed vehicula lacinia nisl, ac placerat arcu ullamcorper at. Pellentesque eleifend, est nec dignissim porta, metus lacus malesuada risus, ut dapibus est libero non diam. Vivamus vestibulum ante id dictum luctus. Pellentesque at scelerisque nisi. Ut scelerisque erat eu sapien aliquam, bibendum rhoncus metus fermentum. Fusce feugiat egestas dui vel lobortis. <br><br> parrafo 2 <br>\
    <div style='text-align: center; font-size: 1.5rem; font-weight: bold;'><br><br> Can technology be used to explore art by the way it makes us feel?</div>\
    </div>",
    unsafe_allow_html=True
)


tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['WikiArt Emotions Dataset', 
                                                    'Workflow',
                                                    'Repository organization',
                                                    'User interaction',
                                                    'Results',
                                                    'Conclusions',
                                                    'Next steps'])
with tab1:

    st.markdown('The data handled in this project is based on the ["WikiArt Emotions"](http://saifmohammad.com/WebPages/wikiartemotions.html) dataset. This dataset was compiled from WikiArt and annotated by crowdworkers for the research [paper](http://saifmohammad.com/WebDocs/lrec2018-paper-art-emotion.pdf) entitled *"WikiArt Emotions: An An Annotated Dataset of Emotions Evoked by Art"*, by Dr. Saif M. Mohammad and Dr. Svetlana Kiritchenko. As a result, 4,019 images were obtained representing 22 categories of four major styles: Renaissance, Post-Renaissance, Modern and Contemporary.')

    def main():
        html_donut= """<div class='tableauPlaceholder' id='viz1686147825076' style='position: relative'><noscript><a href='#'><img alt='DONUT ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;Art22sentiments&#47;DONUT&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Art22sentiments&#47;DONUT' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ar&#47;Art22sentiments&#47;DONUT&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686147825076');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='750px';vizElement.style.maxWidth='800px';vizElement.style.width='100%';vizElement.style.height='777px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='750px';vizElement.style.maxWidth='800px';vizElement.style.width='100%';vizElement.style.height='777px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_donut,width=800, height=700)
    if __name__ =="__main__":
        main()

    st.write('Each artwork in the dataset was annotated by ten crowdworkers, who were presented with a set of 20 emotion words classified as "Positive Emotions", "Negative Emotions" and "Mix/Neutral". The crowdworkers were asked to make annotations based on:')
    st.markdown('''
    - **Scenario I**: presenting only the image of the work (without title)
    - **Scenario II**: presenting only the title of the artwork (no image)
    - **Scenario III**: presenting both the title and the image of the artwork
    ''')

    st.write('In addition, each individual was asked to rate:')
    st.markdown('''
    - The artwork on a scale of -3 (strongly dislike) to 3 (strongly like)
    - Whether the image shows the face/body of a person/animal
    - Whether it is a painting or a different thing (e.g., a sculpture)
    ''')


with tab2:
    st.write('Aquí va una imagen Workflow')

    #df = ('data/WikiArt-Emotions-Clean.csv')
    #st.dataframe(df)

    current_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_path, "../images/workflow/my_image.png")
    st.image(image_path, caption="My Image")


with tab3:
    st.write('Aqui va un listado sobre la organización del repo')
with tab4:
    st.write('aqui va la explicacion de como el usuario interactua con la plataforma')
with tab5:
    st.write('aqui van imagenes de algunos resultados chulis')
with tab6:
    st.write('aqui van mis conclus')
with tab7:
    st.write('aqui mis next steps')

