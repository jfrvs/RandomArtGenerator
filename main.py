import random
import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from random_walk import *
from plot_setup import *

def aspect_ratio_label_fix(aspect_ratio):
    return str(aspect_ratio[0]) + " x " + str(aspect_ratio[1])

def main():
    st.markdown("# RandomWalk Art Generator")
    st.markdown("## Introduction")
    st.markdown("""Hi! Thank you for visiting the RandomWalk Art Generator, a tool which allows you to use random walk to create beautiful images that can be used as wallpapers.\n""")

    # Basic properties

    st.markdown("""First, let's set some image properties.\n""")

    col1, col2, col3 = st.columns(3)
    dpi = col1.selectbox("DPI:", (100, 150, 200, 250, 300, 350, 400), index=4)
    background_color = col2.color_picker("Background Color", "#ffffff")
    aspect_ratio = col3.selectbox("Aspect Ratio:", ([3, 2], [4, 3], [9, 16], [16, 9], [16, 10], [18, 9], [19.5, 9], [21, 9], [32, 9]), index=1, format_func=aspect_ratio_label_fix)
    
    st.markdown("""Each line in our image is of a randomly generated color. We can use the sliders below to alter the shades used to make these colors.\n""")

    st.markdown("""The sliders below damp the presence of a particular shade in the avaliable colors.\n""")
    st.markdown("""Set one slider to zero, for example, and that shade won't be used in the color of the lines.\n""")
    
    col1, col2, col3 = st.columns(3)
    red_d = col1.slider("Red hue damp parameter:", 0.0, 1.0, value=1.0, step=0.01)
    green_d = col2.slider("Green hue damp parameter:", 0.0, 1.0, value=1.0, step=0.01)
    blue_d = col3.slider("Blue hue damp parameter:", 0.0, 1.0, value=1.0, step=0.01)
    
    st.markdown("""The sliders below modify the distribution of a particular shade in the avaliable colors.\n""")
    st.markdown("""Values greater than 1 favour darker shades, values smaller than 1 favour lighter shades.\n""")
    
    col1, col2, col3 = st.columns(3)
    red_p = col1.slider("Red hue distribution parameter:", 0.2, 2.0, value=1.0, step=0.1)
    green_p = col2.slider("Green hue distribution parameter:", 0.2, 2.0, value=1.0, step=0.1)
    blue_p = col3.slider("Blue hue distribution parameter:", 0.2, 2.0, value=1.0, step=0.1)
    
    # Line properties
    
    st.markdown("""You can move the sliders below to modify image zoom, line transparency and line width. Try it out!\n""")
    
    col1, col2, col3 = st.columns(3)
    alpha = col1.slider("Line transparency:", 0.0, 1.0, value=0.50, step=0.01)
    zoom = col2.slider("Zoom:", 0.0, 8.0, value=1.0, step=0.1)
    linewidth = col3.slider("Linewidth:", 0.0, 8.0, value=1.0, step=0.1)

    # Random walk settings

    st.markdown("""The sliders below modify the settings for the random walk algorithm, such as the number of lines that will be drawn, how many steps each line takes, and in how many directions the line can move.\n""")
    
    col1, col2, col3 = st.columns(3)
    possible_directions = col3.selectbox("Number of possible step directions:", (3, 4, 5, 6, 7, 8, 9))
    number_of_walkers = col2.selectbox("Number of lines:", (1, 10, 100, 1000, 10000, 100000))
    number_of_steps = col1.selectbox("Number of steps per line:", (2500, 5000, 7500, 10000, 15000, 20000, 30000, 50000))

    st.markdown("""Now let's make our image. If you don't like what you see, try changing some of the parameters above.\n""")

    st.markdown("""Have fun!\n""")

    # Generate button
    if st.button("Click here to generate image!"):
        with st.spinner("Rendering image..."):
            fig, ax = plot_multiple_walkers(
                number_of_walkers, number_of_steps, 
                red_d, green_d, blue_d, 
                red_p, green_p, blue_p, 
                alpha, possible_directions, linewidth, zoom, 
                aspect_ratio, dpi
            )

            fig.patch.set_facecolor(background_color)
            ax.patch.set_facecolor(background_color)

            st.pyplot(fig)

            # Save and download image
            plt.savefig('my_figure.png', bbox_inches='tight', pad_inches=0)
            with open("my_figure.png", "rb") as file:
                st.download_button(label="Download image", data=file, file_name="my_figure.png", mime="image/png")

if __name__ == '__main__':
    main()
