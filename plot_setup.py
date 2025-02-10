import sys, os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from random_walk import *

def color_profile(red_d, green_d, blue_d, red_p, green_p, blue_p, alpha, number_of_walkers):
    colors = np.zeros((number_of_walkers, 4))  # Create an n×4 array
    colors[:, 0] = red_d * np.random.rand(number_of_walkers) ** red_p  # Red channel
    colors[:, 1] = green_d * np.random.rand(number_of_walkers) ** green_p  # Green channel
    colors[:, 2] = blue_d * np.random.rand(number_of_walkers) ** blue_p  # Blue channel
    colors[:, 3] = alpha  # Alpha channel (same for all)

    return colors

# Plot

def plot_setup(aspect_ratio, dpi):
    plt.rcParams["figure.figsize"] = aspect_ratio
    plt.rcParams["figure.dpi"] = dpi
    fig, ax = plt.subplots()
    
    return fig, ax

def set_axes(walker, aspect_ratio):
    xmax = np.max(walker[:,0])
    xmin = np.min(walker[:,0])
    ymax = np.max(walker[:,1])
    ymin = np.min(walker[:,1])

    x_range = xmax - xmin
    y_range = ymax - ymin

    if y_range/x_range >= aspect_ratio[1]/aspect_ratio[0]:
        mod = (aspect_ratio[0]/aspect_ratio[1])*y_range - x_range
        xmax = xmax + mod/2
        xmin = xmin - mod/2
    else:
        mod = (aspect_ratio[1]/aspect_ratio[0])*x_range - y_range
        ymax = ymax + mod/2
        ymin = ymin - mod/2
    
    return [xmax, xmin, ymax, ymin]

def fix_axes(axis_tuple, aspect_ratio):
    xmax = axis_tuple[0]
    xmin = axis_tuple[1]
    ymax = axis_tuple[2]
    ymin = axis_tuple[3]

    x_range = xmax - xmin
    y_range = ymax - ymin

    if y_range/x_range >= aspect_ratio[1]/aspect_ratio[0]:
        mod = (aspect_ratio[0]/aspect_ratio[1])*y_range - x_range
        xmax = xmax + mod/2
        xmin = xmin - mod/2
    else:
        mod = (aspect_ratio[1]/aspect_ratio[0])*x_range - y_range
        ymax = ymax + mod/2
        ymin = ymin - mod/2
    
    return [xmax, xmin, ymax, ymin]

def plot_multiple_walkers(number_of_walkers, number_of_steps, red_d, green_d, blue_d, red_p, green_p, blue_p, alpha, possible_directions, linewidth, zoom, aspect_ratio, dpi):
    fig, ax = plot_setup(aspect_ratio=aspect_ratio, dpi=dpi)
    
    axis_limit = [0, 0, 0, 0]

    pallete=color_profile(red_d, green_d, blue_d, red_p, green_p, blue_p, alpha, number_of_walkers)

    for i in range(number_of_walkers):
        walker = random_walk(number_of_steps, possible_directions)
        ax.plot(walker[:,0], walker[:,1], color=(pallete[i, 0], pallete[i, 1], pallete[i, 2], pallete[i, 3]), linewidth=linewidth)
        new_axis_limit = set_axes(walker, aspect_ratio)
        if new_axis_limit[0] > axis_limit[0]:
            axis_limit[0] = new_axis_limit[0]
        if new_axis_limit[2] > axis_limit[2]:
            axis_limit[2] = new_axis_limit[2]

        if new_axis_limit[1] < axis_limit[1]:
            axis_limit[1] = new_axis_limit[1]
        if new_axis_limit[3] < axis_limit[3]:
            axis_limit[3] = new_axis_limit[3]
    
    axis_limit = fix_axes(axis_limit, aspect_ratio)
    ax.xaxis.set_data_interval(axis_limit[1]/zoom, axis_limit[0]/zoom, ignore=True)
    ax.yaxis.set_data_interval(axis_limit[3]/zoom, axis_limit[2]/zoom, ignore=True)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    
    return fig, ax
    