import nicenquickplotlib as nq
import uncertainties as unc # https://pythonhosted.org/uncertainties/index.html
import numpy as np

x = np.linspace(0,2,10) # Create x data.
y_vals_1 = x**2 # Create y_1 data.
y_errs_1 = y_vals_1*0.1 + np.random.rand(len(x))*0.1 # Create y_1 errors.
y_vals_2 = np.sqrt(x) # Create y_2 data.
y_errs_2 = y_vals_2*0.1 + np.random.rand(len(x))*0.1 # Create y_2 errors.
y_1 = unc.unumpy.uarray(y_vals_1, y_errs_1) # Create y_1 array of uncertainties.
y_2 = unc.unumpy.uarray(y_vals_2, y_errs_2) # Create y_2 array of uncertainties.
nq.plot(x, [y_1, y_2], title='y error bands', legend=['Data 1', 'Data 2'], marker=True)
nq.set_figstyle('blacknwhite')
nq.plot(x, [y_1, y_2], title='y error bands with blacknwhite figstyle', legend=['Data 1', 'Data 2'], marker=True)
nq.save_all(csv=True)
