import sys
import numpy as np

sys.path.append('..')
import dnplab

filename = '..data/h5/test.h5'

ws = dnplab.dnpImport.h5.loadh5(filename)

dnplab.dnpResults.plot(ws['ft'])
dnplab.dnpResults.xlim(20,-20)
dnplab.dnpResults.figure()
dnplab.dnpResults.plot(ws['proc'], 'o')

dnplab.dnpResults.figure()
ws['ft'].reorder(['power'])
dnplab.dnpResults.imshow(ws['ft'].abs)

dnplab.dnpResults.show()

