"""Construct polynomial from polynomial attributes."""
import numpoly

from . import clean as clean_


def polynomial_from_attributes(
        exponents,
        coefficients,
        indeterminants,
        dtype=None,
        clean=True,
):
    """
    Construct polynomial from polynomial attributes.

    Args:
        exponents (numpy.ndarray):
            The exponents in an integer array with shape ``(N, D)``, where
            ``N`` is the number of terms in the polynomial sum and ``D`` is
            the number of dimensions.
        coefficients (Iterable[numpy.ndarray]):
            The polynomial coefficients. Must correspond to `exponents` by
            having the same length ``N``.
        indeterminants (Union[str, Tuple[str, ...], numpoly.ndpoly]):
            The indeterminants variables, either as string names or as
            simple polynomials. Must correspond to the exponents by having
            length ``D``.
        dtype (Optional[numpy.dtype]):
            The data type of the polynomial. If omitted, extract from
            `coefficients`.
        clean (bool):
            Clean up attributes, removing redundant indeterminants and
            exponents.

    Examples:
        (numpoly.ndpoly):
            Polynomial array with attributes determined by the input.

    """
    if clean:
        exponents, coefficients, indeterminants = clean_.postprocess_attributes(
            exponents, coefficients, indeterminants)
    dtype = coefficients[0].dtype if dtype is None else dtype
    poly = numpoly.ndpoly(
        exponents=exponents,
        shape=coefficients[0].shape,
        indeterminants=indeterminants,
        dtype=dtype,
    )
    for exponent, values in zip(poly.keys, coefficients):
        poly[exponent] = values
    return poly
