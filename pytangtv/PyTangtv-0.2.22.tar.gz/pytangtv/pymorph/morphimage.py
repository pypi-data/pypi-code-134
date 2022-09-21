
import numpy as np
from scipy.interpolate import griddata


def polywarp(xi, yi, xo, yo, degree=1):
    """
        Translated from the IDL procedure polywarp.
        Computes the the polynomial warping function such
        that:
           Xi = sum over i and j of:  Kx[i,j] * Xo^j * Yo^i
           Yi = sum over i and j of:  Ky[i,j] * Xo^j * Yo^i

        The cooeficients Kx and Ky can be used as inputs into
        poly2d to produced a warped image.
    """

    m = len(xi)
    if m != len(xo) or m != len(yi) or m != len(yo):
        raise "Inconsistant number of control points"
    n = degree
    n2 = (n+1)**2
    if n2 > m:
        raise "# of points must be ge (degree+1)^2"
    x = np.array([xi, yi])
    u = np.array([xo, yo])
    ut = np.zeros([n2, m])
    u2i = np.zeros(n+1)
    for i in np.arange(m):
        u2i[0] = 1
        zz = u[1, i]
        for j in np.arange(1, n+1):
            u2i[j] = u2i[j-1]*zz
        ut[0:n+1, i] = u2i
        for j in np.arange(1, n+1):
            t = u2i*u[0, i]**j
            ut[j*(n+1):j*(n+1)+n+1, i] = u2i*u[0, i]**j

    uu = np.dot(ut, ut.T).T
    kk = np.linalg.inv(uu)
    kk = np.dot(kk.T, ut)
    kx = np.dot(kk, x[0, :].T).reshape(n+1, n+1)
    ky = np.dot(kk, x[1, :].T).reshape(n+1, n+1)
    return kx, ky


def poly_2d(a, kx, ky):
    ylen, xlen = a.shape
    degree = len(kx)-1

    yo, xo = np.mgrid[0:ylen, 0:xlen]
    xi = np.zeros((ylen,xlen))
    yi = np.zeros((ylen,xlen))

    for i in np.arange(degree+1):
        for j in np.arange(degree+1):
            xi = xi + kx[j, i]*(xo**j)*(yo**i)
            yi = yi + ky[j, i]*(xo**j)*(yo**i)

    points = np.array([yo.reshape(xlen*ylen),xo.reshape(xlen*ylen)]).T
    ao = griddata(points, a.reshape(xlen*ylen), (yi, xi), method='nearest', fill_value=0)
    return ao

def poly_pt(xpt,ypt,kx,ky):
    degree = len(kx)-1

    xi = 0.0
    yi = 0.0
    for i in np.arange(degree+1):
        for j in np.arange(degree+1):
            xi = xi + kx[j, i]*(xpt**j)*(ypt**i)
            yi = yi + ky[j, i]*(xpt**j)*(ypt**i)

    return xi,yi





