# Nice 'n quick plot lib
Package to produce nice plots quickly using matplotlib.

This package contains a set of functions to help the user to produce nice plots without having to worry about formatting them. It uses matplotlib to produce high quality plots. There are a set of "default config params" that can be modified in order that all plots to have the same format.

## Instalation
- Python 2
```
pip install git+https://github.com/SengerM/nicenquickplotlib.git
```
- Python 3
```
pip3 install git+https://github.com/SengerM/nicenquickplotlib.git
```

## Usage
```Python
import nicenquickplotlib as nq
import numpy as np
x = np.linspace(0,10)
nq.plot(np.sin(x))
nq.show()
```
