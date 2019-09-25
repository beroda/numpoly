"""View inputs as arrays with at least three dimensions."""
import numpy
import numpoly

from .common import implements


@implements(numpy.atleast_3d)
def atleast_3d(*arys):
    """
    View inputs as arrays with at least three dimensions.

    Args:
        arys (numpoly.ndpoly):
            One or more array-like sequences. Non-array inputs are converted
            to arrays. Arrays that already have three or more dimensions are
            preserved.

    Returns:
        (numpoly.ndpoly):
            An array, or list of arrays, each with ``a.ndim >= 3``.  Copies are
            avoided where possible, and views with three or more dimensions are
            returned.  For example, a 1-D array of shape ``(N,)`` becomes
            a view of shape ``(1, N, 1)``, and a 2-D array of shape ``(M, N)``
            becomes a view of shape ``(M, N, 1)``.

    Examples:
        >>> numpoly.atleast_3d(numpoly.symbols("x"))
        polynomial([[[x]]])
        >>> numpoly.atleast_3d(1, [2, 3])
        [polynomial([[[1]]]), polynomial([[[2],
                     [3]]])]

    """
    arys = [numpoly.aspolynomial(ary) for ary in arys]
    arys = [ary.reshape(1, 1, 1) if ary.ndim == 0 else ary for ary in arys]
    arys = [ary[numpy.newaxis, :, numpy.newaxis] if ary.ndim == 1 else ary for ary in arys]
    arys = [ary[:, :, numpy.newaxis] if ary.ndim == 2 else ary for ary in arys]
    if len(arys) == 1:
        return arys[0]
    return arys
