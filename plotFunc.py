"""
Title: Function Plotter
Author: Dominic Vicharelli
Description: plot elementary fuctions along with their Taylor Series approximations
    Uses MatPlotLib for plotting.

Classes heirarchy:
    | PlotFunction
    |       | PlotBaseTrig
    |       |       | PlotTaylorTrig
    |       | PlotExp
    |       |       | PlotTaylorExp
"""
import numpy as np
import taylor

PI = np.pi
PI_CHAR = '\u03C0'


class PlotFunction(object):
    """
    Base class for plotting any function on a given interval
    using axes object.
    """
    def __init__(self, ax, interval):
        self.ax = ax
        self.interval = interval


class PlotBaseTrig(PlotFunction):
    """
    Class for plotting any trig functions (sin() / cos())
    """
    def __init__(self, ax, interval):
        """
        interval is total length of interval in terms of pi. e.g. 4 -> [-2pi, 2pi]
        """
        super().__init__(ax, interval)
        self.x_vals = self.get_trig_x_vals()

    def __trig_x_ticks(self) -> list:
        """ helper function for setting x tick locations.

            interval_len is length of interval in terms of pi. e.g. 4 -> (4 * PI)
            return list of x-value tick marks for trig functions (float values)
            the amount of tick marks is always double the interval plus one. e.g. 4 -> 9 ticks
        """
        x_ticks = []

        # arithmetic here is to avoid floats in the for loop
        ray = self.interval // 2
        start = -10 * ray
        end = (ray*10) + 5
        for i in range(start, end, 5):
            x_ticks.append((i/10) * PI)

        return x_ticks

    def __trig_x_ticklabels(self) -> list:
        """ helper function for setting x tick labels.

            interval_len is legnth of interval in terms of pi. e.g. 4 -> (4 * PI)
            return list of x-value tick labels for trig functions (strings)
            the amount of tick marks is always double the interval plus one
        """
        x_tick_labels = []

        ray = self.interval // 2
        start = -10 * ray
        end = (ray * 10) + 5

        for i in range(start, end, 5):
            if i == 0:
                label = '0'
            elif i % 2 == 0:
                label = f"{int(i/10)}{PI_CHAR}"
            else:
                label = f"{int(i/5)}{PI_CHAR}/2"

            x_tick_labels.append(label)

        return x_tick_labels

    def __set_trig_plot(self):
        """
        helper function that sets certain plot attributes for trig functions
        """
        if self.interval % 2 == 1 or self.interval <= 0:
            raise Exception('interval must be an even number > 0.')

        y_ticks = []
        for i in range(-5, 6):
            y_ticks.append(i)
        self.ax.set_yticks(y_ticks)
        self.ax.set_xticks(self.__trig_x_ticks())
        self.ax.set_xticklabels(self.__trig_x_ticklabels())
        return

    def get_trig_x_vals(self) -> np.ndarray:
        """
        helper function to get array of x-values used for trig plots
        """
        ray = self.interval / 2
        x_vals = np.linspace((-1 * ray * PI), ray * PI, 100)
        return x_vals

    def plot_sine(self) -> list:
        """
        function to plot sine wave. returns list of Line2D objects
        """
        self.__set_trig_plot()
        y_vals = np.sin(self.x_vals)
        lines = self.ax.plot(self.x_vals, y_vals, label="sin(x)", linewidth="2.5")
        return lines

    def plot_cosine(self) -> list:
        """
        function to plot cosine wave. returns list of Line2D objects
        """
        self.__set_trig_plot()
        y_vals = np.cos(self.x_vals)
        lines = self.ax.plot(self.x_vals, y_vals, label="cos(x)", linewidth="2.5")
        return lines


class PlotTaylorTrig(PlotBaseTrig):
    """
    class for plotting Taylor Series approximations for trig functions.
    no plot initaliziation happens in this class, only plotting (since the Taylor Series
    will never be plotted on its own)
    """
    def __init__(self, ax, interval):
        super().__init__(ax, interval)
        self.x_vals = super().get_trig_x_vals()

    def plot_sine_approx(self, n: int) -> list:
        """
        plot nth degree taylor series for sine function centered at 0.
        returns list of Line2D objects.
        """
        y_vals = []
        for num in np.nditer(self.x_vals):
            y_vals.append(taylor.sine_approx(n, num))
        lines = self.ax.plot(self.x_vals, y_vals, label=f"Taylor Series degree {n}")
        return lines

    def plot_cosine_approx(self, n: int) -> list:
        """
        plot nth degree taylor series for cosine function centered at 0.
        returns list of Line2D objects
        """
        y_vals = []
        for num in np.nditer(self.x_vals):
            y_vals.append(taylor.cosine_approx(n, num))
        lines = self.ax.plot(self.x_vals, y_vals, label=f"Taylor Series degree {n}")
        return lines


class PlotExp(PlotFunction):
    """
    Class for plotting the exponential function e^x
    """
    def __init__(self, ax, interval):
        super().__init__(ax, interval)
        self.x_vals = np.linspace((-2 * self.interval), 2 * self.interval, 100)

    def __exp_x_ticklabels(self) -> list:
        """
        helper function for setting x tick labels.
        return list of x-value tick labels for exp function (strings)
        the amount of tick marks is always twice the interval plus one
        """
        x_tick_labels = []
        for i in range(-1*self.interval, self.interval):
            x_tick_labels.append(i)
        return x_tick_labels

    def __set_exp_plot(self):
        """
        helper function that sets certain plot attributes for the exponential function
        """
        y_ticks = []
        for i in range(-5, 6):
            y_ticks.append(i)
        self.ax.set_yticks(y_ticks)

    def plot_exp(self) -> list:
        """
        function to plot exponential curve. returns list of Line2D objects
        """
        self.__set_exp_plot()
        y_vals = np.exp(self.x_vals)
        lines = self.ax.plot(self.x_vals, y_vals, label="e^(x)", linewidth="2.5")
        return lines


class PlotTaylorExp(PlotExp):
    """
    class for plotting Taylor Series approximations for the exponential function.
    no plot initaliziation happens in this class, only plotting (since the Taylor Series
    will never be plotted on its own)
    """
    def __init__(self, ax, interval):
        super().__init__(ax, interval)

    def plot_exp_approx(self, n: int) -> list:
        """
        plot nth degree taylor series for exponential function centered at 0.
        returns list of Line2D objects
        """
        y_vals = []
        for num in np.nditer(self.x_vals):
            y_vals.append(taylor.exp_approx(n, num))
        lines = self.ax.plot(self.x_vals, y_vals, label=f"Taylor Series degree {n}")
        return lines




