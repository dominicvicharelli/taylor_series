# Interactive Taylor Series 

This project is based off of the paper that I wrote included in this 
repository (called e^x.pdf) that gives a very in-depth approach to 
understanding Taylor Series approximations. The paper builds an understanding
from the bottom up, making it understandable to anyone who has the slightest
exposure to basic calculus. The python project uses the MatPlotLib library
to plot an interactive Taylor Series graph for a few elementary functions.

## Getting Started

Perform the following steps for a local, interactive copy of the project. Otherwise, screenshots of the interactive graph are posted at the end of this file. 

Clone the repository with the url: `https://github.com/dominicvicharelli/taylor_series.git`

Download MatPlotLib from the command line using pip:
``` pip install -U matplotlib ```

From the command line, navigate to local folder which contains project and simply execute main.py:
```python main.py [interval]```
* For best graphing results, interval must be 2, 4, 6, or 8 if specified. By default, interval is set to 4.


## Screenshots
![Sine wave gif](https://github.com/dominicvicharelli/taylor_series/raw/master/gifs/sin.gif)

![Cosine wave gif](https://github.com/dominicvicharelli/taylor_series/raw/master/gifs/cos.gif)

![e^x gif](https://github.com/dominicvicharelli/taylor_series/raw/master/gifs/e.gif)
