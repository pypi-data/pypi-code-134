#!/usr/bin/env python

import numpy
from matplotlib import pyplot
import gemmi

# toxd_aupatt.map is generated by $CCP4/examples/unix/runnable/patterson
ccp4 = gemmi.read_ccp4_map('/tmp/wojdyr/toxd_aupatt.map', setup=True)
arr = numpy.array(ccp4.grid, copy=False)
x = numpy.linspace(0, ccp4.grid.unit_cell.a, num=arr.shape[0], endpoint=False)
y = numpy.linspace(0, ccp4.grid.unit_cell.b, num=arr.shape[1], endpoint=False)
X, Y = numpy.meshgrid(x, y, indexing='ij')
pyplot.contour(X, Y, arr[:,:,40])
pyplot.gca().set_aspect('equal', adjustable='box')
pyplot.show()
