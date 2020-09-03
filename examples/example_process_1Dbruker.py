# DNPLab example script to import 1D Bruker data, process FID and display NMR spectrum

# Import python modules

import sys
import numpy as np

sys.path.append('..')
import dnplab

# Import data
path = '\path\to\topsin\data\'
folder = 20
data = dnplab.dnpImport.topspin.import_topspin(path,folder)

# Create workspace
ws = dnplab.create_workspace()
ws.add('raw', data)
ws.copy('raw', 'proc')

# Process FID and display spectrum
dnplab.dnpNMR.remove_offset(ws,{})
dnplab.dnpNMR.window(ws,{'linewidth' : 10})
dnplab.dnpNMR.fourier_transform(ws,{'zero_fill_factor' : 2})
dnplab.dnpNMR.autophase(ws,{})

dnplab.dnpResults.figure()
dnplab.dnpResults.plot(ws['proc'].real)
dnplab.dnpResults.xlim([-35,50])
dnplab.dnpResults.plt.xlabel('Chemical Shift [ppm]')
dnplab.dnpResults.plt.ylabel('Signal Amplitude [a.u.]')
dnplab.dnpResults.show()