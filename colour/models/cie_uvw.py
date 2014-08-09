#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**cie_uvw.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package colour *CIE UVW* colourspace objects.

**Others:**

"""

from __future__ import unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models import UCS_to_uv, XYZ_to_UCS, XYZ_to_xyY, xy_to_XYZ

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["XYZ_to_UVW"]


def XYZ_to_UVW(XYZ,
               illuminant=ILLUMINANTS.get(
                   "CIE 1931 2 Degree Standard Observer").get("D50")):
    """
    Converts from *CIE XYZ* colourspace to *CIE 1964 U\*V*\W\** colourspace.

    Examples::

        >>> XYZ_to_UVW(np.array([11.80583421, 10.34, 5.15089229]))
        array([[ 24.25433719]
               [  7.22054843]
               [ 37.46450007]])

    :param XYZ: *CIE XYZ* colourspace matrix.
    :type XYZ: array_like, (3, 1)
    :param illuminant: Reference *illuminant* chromaticity coordinates.
    :type illuminant: array_like
    :return: *CIE 1964 U\*V*\W\** colourspace matrix.
    :rtype: ndarray, (3, 1)

    :warning: The arguments domains of that definition are non standard!
    :note: Input *CIE XYZ* colourspace matrix is in domain [0, 100].
    :note: Output *CIE UVW* colourspace matrix is in domain [0, 100].

    References:

    -  http://en.wikipedia.org/wiki/CIE_1964_color_space \
    (Last accessed 10 June 2014)
    """

    x, y, Y = np.ravel(XYZ_to_xyY(XYZ, illuminant))
    u, v = np.ravel(UCS_to_uv(XYZ_to_UCS(XYZ)))
    u0, v0 = np.ravel(UCS_to_uv(XYZ_to_UCS(xy_to_XYZ(illuminant))))

    W = 25. * Y ** (1. / 3.) - 17.
    U = 13. * W * (u - u0)
    V = 13. * W * (v - v0)

    return np.array([U, V, W]).reshape((3, 1))