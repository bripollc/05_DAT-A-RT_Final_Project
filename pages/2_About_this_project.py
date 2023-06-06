import streamlit as st


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
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mi elit, varius vel dapibus eget, facilisis sit amet nisl. Mauris nec tristique eros. Etiam molestie mauris a urna gravida, et molestie justo dignissim. Praesent id quam id eros dignissim ultricies. Pellentesque rhoncus odio quis diam dictum mollis. Vivamus ac eleifend lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed vehicula lacinia nisl, ac placerat arcu ullamcorper at. Pellentesque eleifend, est nec dignissim porta, metus lacus malesuada risus, ut dapibus est libero non diam. Vivamus vestibulum ante id dictum luctus. Pellentesque at scelerisque nisi. Ut scelerisque erat eu sapien aliquam, bibendum rhoncus metus fermentum. Fusce feugiat egestas dui vel lobortis.Vestibulum tempor mollis pulvinar. Mauris tempus fermentum odio sit amet mattis. Nulla aliquet venenatis purus, eu bibendum nisl ultricies eget. Nam elit quam, pellentesque at molestie eu, mollis rutrum massa. Vivamus eget pellentesque urna. Quisque ac diam ex. Aliquam non tellus blandit, blandit turpis quis, tincidunt eros.')
with tab2:
    st.write('Aquí va una imagen Workflow')
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

