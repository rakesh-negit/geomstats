import os
import sys

_default_backend = 'numpy'
if 'GEOMSTATS_BACKEND' in os.environ:
    _backend = os.environ['GEOMSTATS_BACKEND']

else:
    _backend = _default_backend

_BACKEND = _backend

if _BACKEND == 'numpy':
    sys.stderr.write('Using numpy backend\n')
    from .numpy import *  # NOQA
    from . import numpy_random as random
    from . import numpy_linalg as linalg
elif _BACKEND == 'tensorflow':
    sys.stderr.write('Using tensorflow backend\n')
    from .tensorflow import *  # NOQA
    from . import tensorflow_random as random
    from . import tensorflow_linalg as linalg
elif _BACKEND == 'pytorch':
    raise NotImplementedError('pytorch backend not implemented yet')


def backend():
    return _BACKEND
