# Nice 'n quick plot lib
Package to produce nice plots quickly using matplotlib

This package contains a set of functions to help the user to produce nice plots without much effort. It uses matplotlib to produce high quality plots.

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
