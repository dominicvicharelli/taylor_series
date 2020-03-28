"""
Title: Taylor Series Approximation Visualization
Author: Dominic Vicharelli
Description: See how closely elementary functions are approximated by their
    corresponding Taylor Series expansion through an interactive graph interface.
    Choose which elementary function you want to approximate (sin(x), cos(x), or e^(x)),
    and to what degree of accuracy with the interactive radio buttons and slider.

    This program uses MatPlotLib as its main plotting library.
    Plotting is done with the object oriented approach instead of MATLAB style using pyplot
"""

import matplotlib.pyplot as plt
import plotFunc
import plotInit


def update_slider(val):
    """
    function that is executed upon slider move (val corresponds to integer value of slider).
    clears previous Taylor approximation and plots new one
    """
    # the taylor lines object is the fourth object in ax.lines since:
    # ax.lines = [y=0 line, x=0 line, base function line, taylor line]
    ax.lines.remove(ax.lines[3])

    label_check = ax.lines[2].get_label()
    if label_check == 'sin(x)':
        trig_approx.plot_sine_approx(int(val))
    elif label_check == 'cos(x)':
        trig_approx.plot_cosine_approx(int(val))
    elif label_check == 'e^(x)':
        exp_approx.plot_exp_approx(int(val))
    ax.legend()
    fig.canvas.draw_idle()


def update_graph(label):
    """
    function that is executed upon radio button selection.
    label corresponds to string label of currently selected graph
    """
    # clear previous function and its taylor series
    slider.reset()
    ax.lines.remove(ax.lines[3])
    ax.lines.remove(ax.lines[2])

    # plot new graph with taylor approximation
    if label == 'e^(x)':
        exp_function.plot_exp()
        exp_approx.plot_exp_approx(1)
    elif label == 'sin(x)':
        trig_function.plot_sine()
        trig_approx.plot_sine_approx(1)
    elif label == 'cos(x)':
        trig_function.plot_cosine()
        trig_approx.plot_cosine_approx(1)

    ax.legend()
    fig.canvas.draw_idle()


# initialize figure, axes, slider, and radio
fig, ax = plotInit.init_plot()
slider = plotInit.create_slider()
radio = plotInit.create_radio()

interval = 6

trig_function = plotFunc.PlotBaseTrig(ax, interval)
trig_approx = plotFunc.PlotTaylorTrig(ax, interval)
exp_function = plotFunc.PlotExp(ax, interval)
exp_approx = plotFunc.PlotTaylorExp(ax, interval)

# initialize graph with sin wave
trig_function.plot_sine()
trig_approx.plot_sine_approx(1)

slider.on_changed(update_slider)
radio.on_clicked(update_graph)
ax.legend()
plt.show()

