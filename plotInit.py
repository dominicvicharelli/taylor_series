"""
Title: Plot Initializer
Author: Dominic Vicharelli
Description: initializes plot by creating figure, axes, slider, and radio buttons.
    For more information on how MatPlotLib organization, view the figure from source:
    https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
"""

from matplotlib.widgets import Slider, RadioButtons
import matplotlib.pyplot as plt


def init_plot():
    """ create figure and axes object, set basic plot attributes """
    fig, ax = plt.subplots()
    fig.suptitle('Taylor Series Approximations')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which="both", axis="both", linestyle='dashed')
    ax.autoscale(False)
    return fig, ax


def create_slider():
    """
    make room in plot for slider at bottom of graph, and
    create new axes in figure called 'nax' for slider.
    documentation for axes method: plt.axes([left, bottom, width, height], **kwargs)
    """
    plt.subplots_adjust(bottom=0.2)
    nax = plt.axes([0.2, 0.07, 0.65, 0.03], facecolor='0.9')
    slider = Slider(nax, 'nth degree', 1, 20, 1, valstep=1)
    return slider


def create_radio():
    """
    make room in plot for radio buttons left of graph, and
    create new axes in figure called 'rax' for radio buttons.
    documentation for axes method: plt.axes([left, bottom, width, height], **kwargs)
    """
    plt.subplots_adjust(left=0.2)
    rax = plt.axes([0.04, .7, 0.1, 0.15], facecolor='0.9')
    radio = RadioButtons(rax, ('sin(x)', 'cos(x)', 'e^(x)'))
    return radio



