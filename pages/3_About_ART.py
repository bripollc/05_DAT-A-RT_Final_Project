import streamlit as st

st.set_page_config(page_title = "DAT(A)RT", page_icon = ":sunglasses:")

st.title("ART")
st.markdown("explore the different movements that are collected in the dataset:")


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22 = st.tabs(['Abstract Art', 
                                                                                                                                                            'Abstract Expressionism',
                                                                                                                                                            'Art Informel',    
                                                                                                                                                            'Baroque',
                                                                                                                                                            'Color Field Painting',    
                                                                                                                                                            'Cubism',
                                                                                                                                                            'Early Renaissance',    
                                                                                                                                                            'Expressionism',
                                                                                                                                                            'High Renaissance',    
                                                                                                                                                            'Impressionism',
                                                                                                                                                            'Lyrical Abstraction',    
                                                                                                                                                            'Magic Realism',
                                                                                                                                                            'Minimalism',    
                                                                                                                                                            'Neo Expressionism',
                                                                                                                                                            'Neoclassicism',    
                                                                                                                                                            'Northern-Renaissance',
                                                                                                                                                            'Pop Art',
                                                                                                                                                            'Post Impressionism', 
                                                                                                                                                            'Realism',
                                                                                                                                                            'Rococo',    
                                                                                                                                                            'Romanticism',
                                                                                                                                                            'Surrealism'])                     
                                                                                                                                                           


# Abstract Art
with tab1:
    st.write ('Abstract Art emerged in the early 20th century, around 1910. It is characterized by a departure from representing recognizable objects or figures and instead emphasizes the use of color, form, line, and texture to create compositions that exist purely for their own sake.')
    st.write ('Abstract Art encompasses a wide range of styles and approaches, from Wassily Kandinsky\'s pioneering non-representational works to the geometric abstractions of Piet Mondrian. Notable abstract artists include Kazimir Malevich, Joan Miró, and Mark Rothko.')
    st.image('https://uploads8.wikiart.org/images/jock-macdonald/fluctuating-planes-1952.jpg')
    st.text('Jock Macdonald: Fluctuating Planes - 1952')
# Abstract Expressionism
with tab2:
    st.write ('Abstract Expressionism developed in the United States in the late 1940s and early 1950s. It is known for its spontaneous and gestural approach to painting, often characterized by large-scale works with bold brushwork and expressive use of color.')
    st.write ('Abstract Expressionists sought to convey emotion and subjective experience through their art. Key figures in this movement include Jackson Pollock, Willem de Kooning, and Mark Rothko.')
    st.image('https://uploads4.wikiart.org/images/willem-de-kooning/woman-i.jpg')
    st.text('Willem de Kooning: Woman I - 1952')
# Art Informel
with tab3:
    st.write ('Art Informel, also known as Tachisme, emerged in Europe after World War II, around the late 1940s and early 1950s. It is characterized by its emphasis on spontaneity, intuitive gestures, and the exploration of the subconscious. Artists associated with Art Informel, such as Jean Dubuffet and Antoni Tàpies, sought to create works that embodied raw emotion and the chaotic nature of existence. The movement embraced a variety of techniques, including gestural brushwork, collage, and assemblage.')
    st.image('https://uploads7.wikiart.org/images/karel-appel/people-birds-and-sun-1954.jpg')
    st.text('Karel Appel: People, Birds and Sun - 1954')
# Baroque
with tab4:
    st.write ('The Baroque period flourished from the late 16th century to the early 18th century, originating in Italy and spreading throughout Europe. Baroque art is characterized by its grandeur, theatricality, and elaborate ornamentation. It sought to evoke strong emotions and create a sense of awe through dramatic compositions, intricate details, and the use of light and shadow. Prominent Baroque artists include Gian Lorenzo Bernini, Caravaggio, and Peter Paul Rubens.')
    st.image('https://uploads4.wikiart.org/images/anthony-van-dyck/self-portrait-with-a-sunflower-1632.jpg')
    st.text('Anthony van Dyck: Self portrait with a Sunflower - 1632')
# Color Field Painting 
with tab5:
    st.write ('Color Field Painting emerged in the late 1940s and 1950s as a branch of Abstract Expressionism. It focuses on large areas of flat, solid color that cover the entire canvas, with minimal use of brushwork or surface texture. Color Field painters, such as Mark Rothko and Helen Frankenthaler, aimed to evoke emotional responses through the arrangement of color and the interaction of hues. The movement emphasizes the purity and luminosity of color, often creating a contemplative and immersive experience for the viewer.')
    st.image('https://uploads2.wikiart.org/images/morris-louis/where-1960.jpg')
    st.text('Morris Louis: Where - 1960')

# Cubism
with tab6:
    st.write ('Cubism emerged in the early 20th century, around 1907. It was a revolutionary movement pioneered by Pablo Picasso and Georges Braque. Cubist artists aimed to depict the multiple viewpoints of an object simultaneously, breaking it down into geometric shapes and fragmented forms. They emphasized the two-dimensionality of the canvas and challenged traditional perspective. Cubism laid the foundation for abstract art and greatly influenced modern art movements.')
    st.image('https://uploads0.wikiart.org/images/pablo-picasso/the-girls-of-avignon-1907.jpg')
    st.text('Pablo Picasso: The girls of Avignon - 1907')

# Early Renaissance
with tab7:
    st.write ('The Early Renaissance refers to a period of artistic and cultural rebirth that took place in Europe between the 14th and 15th centuries. It marked a shift from the medieval to the modern world. Artists during this time, such as Giotto di Bondone and Masaccio, focused on naturalism, perspective, and the human form. They aimed to revive the classical ideals of ancient Greece and Rome while incorporating their own artistic innovations.')
    st.image('https://uploads5.wikiart.org/images/sandro-botticelli/the-birth-of-venus-1485(1).jpg')
    st.text('Sandro Botticelli: The Birth of Venus - 1485')

# Expressionism
with tab8:
    st.write ('Expressionism emerged in the early 20th century, with notable developments around 1905. This movement sought to convey subjective emotions and explore the human experience through distorted or exaggerated forms and intense colors. Expressionist artists, including Edvard Munch and Ernst Ludwig Kirchner, rejected the objective depiction of reality and instead focused on conveying the inner turmoil and psychological states of their subjects.')
    st.image('https://uploads1.wikiart.org/images/edvard-munch/the-scream-1893(2).jpg')
    st.text('Edvard Munch: The Scream - 1893')

# High Renaissance
with tab9:
    st.write ('The High Renaissance occurred during the late 15th and early 16th centuries in Italy, reaching its peak around the early 1500s. It is characterized by the work of renowned artists such as Leonardo da Vinci, Michelangelo, and Raphael. The High Renaissance emphasized balance, harmony, and a mastery of technical skills. Artists of this period created iconic works that epitomized ideals of beauty, humanism, and perfection in art.')
    st.image('https://uploads0.wikiart.org/images/michelangelo/sistine-chapel-ceiling-creation-of-adam-1510.jpg')
    st.text('Michelangelo: Sistine Chapel Ceiling:Creation of Adam - 1510')

# Impressionism
with tab10:
    st.write ('Impressionism emerged in the mid-19th century, particularly in France during the 1860s. Artists like Claude Monet, Pierre-Auguste Renoir, and Edgar Degas sought to capture the fleeting effects of light and atmosphere in their paintings. They abandoned detailed brushwork and instead used loose, rapid brushstrokes to convey the impression of a scene or moment. Impressionists often painted en plein air (outdoors) to capture the natural light and shifting colors.')
    st.image('https://uploads0.wikiart.org/images/edouard-manet/a-bar-at-the-folies-bergere-1882-1.jpg')
    st.text('Edouard Manet: A Bar at the Folies-Bergere - 1882')

# Lyrical Abstraction
with tab11:
    st.write ('Lyrical Abstraction is an abstract art movement that emerged in the mid-20th century, around the 1960s. It emphasized intuitive and expressive gestures, exploring color, line, and form to evoke emotions and sensations. Lyrical Abstraction bridged the gap between gestural abstraction and color field painting, incorporating elements of both. Artists associated with Lyrical Abstraction include Joan Mitchell, Sam Francis, and Helen Frankenthaler.')
    st.image('https://uploads2.wikiart.org/images/sam-francis/untitled-yellow-1961.jpg')
    st.text('Sam Francis: Untitled (Yellow) - 1960/1961')

# Magic Realism
with tab12:
    st.write ('Magic Realism is an artistic movement that emerged in the early 20th century, particularly associated with Latin American literature and visual arts. It combines realistic elements with fantastical or magical elements, blurring the boundaries between reality and imagination. Magic Realism seeks to create a sense of wonder and mystery within everyday scenes. Artists such as Frida Kahlo and Salvador Dalí incorporated elements of Magic Realism into their works, presenting dreamlike or surreal imagery within recognizable settings.')
    st.image('https://uploads5.wikiart.org/00150/images/antonio-lopez/atocha-1964.jpg')
    st.text('Antonio Lopez Garcia: Atocha - 1964')

# Minimalism
with tab13:
    st.write ('Minimalism originated in the 1960s as a reaction against the complexity and emotionalism of abstract expressionism. It is characterized by extreme simplicity and a reduction of form to its essential elements. Minimalist artists, such as Donald Judd and Agnes Martin, sought to eliminate any excess and focus on geometric shapes, clean lines, and a limited color palette. Minimalism aimed to create a direct and objective experience for the viewer, often emphasizing the physical presence and materiality of the artwork.')
    st.image('https://uploads2.wikiart.org/images/dan-flavin/untitled-to-henri-matisse-1964.jpg')
    st.text('Dan Flavin: Untitled (to Henri Matisse) - 1964')

# Neo-Expressionism
with tab14:
    st.write ('Neo Expressionism emerged in the late 1970s and early 1980s as a reaction against the formalism and intellectualism of minimalist and conceptual art. It revitalized the expressive qualities of painting, often using bold and gestural brushwork, vivid colors, and intense emotions. Neo-Expressionist artists, like Jean-Michel Basquiat and Anselm Kiefer, sought to engage with personal, cultural, and political issues in their works. They often conveyed raw energy and a sense of urgency in their artistic expressions.')
    st.image('https://uploads4.wikiart.org/images/philip-guston/joys-eating.jpg')
    st.text('Philip Guston: Painting, Smoking, Eating - 1972')

# Neoclassicism
with tab15:
    st.write ('Neoclassicism emerged in the mid-18th century as a reaction against the ornate and elaborate style of the Baroque period. It drew inspiration from the art and aesthetics of ancient Greece and Rome, emphasizing simplicity, clarity, and rationality. Neoclassical artists, such as Jacques-Louis David and Antonio Canova, sought to revive the ideals of classical antiquity and promoted a return to order and reason in art. Neoclassicism often depicted heroic figures, historical events, and moral themes.')
    st.image('https://uploads2.wikiart.org/00118/images/anton-raphael-mengs/carlos-iii-1761.jpg')
    st.text('Anton Raphael Mengs: Carlos III - 1761')

# Northern Renaissance
with tab16:
    st.write ('The Northern Renaissance refers to the artistic and cultural movement that took place in Northern Europe during the 15th and 16th centuries. It emerged as a distinct artistic style alongside the Italian Renaissance. Northern Renaissance artists, including Jan van Eyck and Albrecht Dürer, focused on meticulous detail, naturalistic observation, and the representation of everyday life. They often depicted religious themes, landscapes, and portraiture, incorporating rich symbolism and intricate symbolism into their works.')
    st.image('https://uploads6.wikiart.org/images/hieronymus-bosch/the-garden-of-earthly-delights-1515-7.jpg')
    st.text('Hieronymus Bosch: The Garden of Earthly Delights - 1510/1515')


# Pop Art
with tab17:
    st.write ('Pop Art emerged in the 1950s and 1960s, particularly in the United States and the United Kingdom. It drew inspiration from popular culture and mass media, incorporating imagery from advertising, comic books, and consumer products into fine art. Pop artists, such as Andy Warhol and Roy Lichtenstein, celebrated the aesthetics of consumerism and questioned the boundaries between high and low art. They employed vibrant colors, bold compositions, and mass production techniques to create artworks that reflected the vibrant and consumer-driven society of the time.')
    st.image('https://uploads6.wikiart.org/images/roy-lichtenstein/crying-girl-1964(1).jpg')
    st.text('Roy Lichtenstein: Crying girl - 1964')

# Post-Impressionism
with tab18:
    st.write ('Post-Impressionism emerged in the late 19th century as a reaction against the limitations of Impressionism. Artists such as Paul Cézanne, Vincent van Gogh, and Georges Seurat explored new ways to represent form, color, and perspective. Post-Impressionists maintained the use of vibrant color and visible brushwork but also focused on subjective expression and the underlying structure of their subjects. The movement laid the groundwork for the development of modern art.')
    st.image('https://uploads3.wikiart.org/00142/images/vincent-van-gogh/the-starry-night.jpg')
    st.text('Vincent van Gogh: The Starry Night - 1889')


# Realism
with tab19:
    st.write ('Realism emerged in the mid-19th century as a reaction against the idealized and romanticized styles of the time. Realist artists aimed to depict the ordinary world with accuracy and truthfulness. They focused on everyday subjects, including landscapes, urban scenes, and scenes of working-class life. Prominent Realist artists include Gustave Courbet, Jean-François Millet, and Honoré Daumier.')
    st.image('https://uploads5.wikiart.org/images/gustave-courbet/the-origin-of-the-world-1866.jpg')
    st.text('Gustave Courbet: The Origin of the World - 1866')


# Rococo
with tab20:
    st.write ('Rococo was an art movement that flourished in the 18th century, particularly in France. It is characterized by its decorative and ornamental style, featuring intricate patterns, delicate forms, and a lighthearted and playful tone. Rococo art often depicted scenes of leisure, romance, and fantasy. François Boucher and Jean-Honoré Fragonard were prominent Rococo artists known for their elegant and charming works.')
    st.image('https://uploads6.wikiart.org/images/jean-honore-fragonard/the-swing-1767.jpg')
    st.text('Jean-Honore Fragonard: The Swing - 1767')


# Romanticism
with tab21:
    st.write ('Romanticism emerged in the late 18th century as a reaction against the rationality and restraint of the Enlightenment period. It emphasized individualism, emotion, imagination, and a connection with nature. Romantic artists sought to evoke strong emotional responses through dramatic and sublime landscapes, historical events, and scenes of heroism. Notable Romantic artists include Caspar David Friedrich, J.M.W. Turner, and Eugène Delacroix.')
    st.image('https://uploads1.wikiart.org/images/theodore-gericault/the-raft-of-the-medusa-1819(1).jpg')
    st.text('Theodore Gericault: The Raft of the Medusa - 1818/1819')


# Surrealism
with tab22:
    st.write ('Surrealism emerged in the early 20th century as a literary and artistic movement. It sought to explore the realm of the subconscious and trigger the power of the imagination. Surrealist artists, such as Salvador Dalí, René Magritte, and Max Ernst, created dreamlike and bizarre imageges, often combining unrelated elements to challenge the conventional understanding of reality. Surrealism aimed to access the hidden aspects of the human psyche and tap into the irrational.')
    st.image('https://uploads5.wikiart.org/images/salvador-dali/the-persistence-of-memory-1931.jpg')
    st.text('Salvador Dali: The Persistence of Memory - 1931')

