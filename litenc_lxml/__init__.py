import sys
from litenc_lxml import litenc_lxml

if sys.version_info < (2, 6):
    raise RuntimeError('You need Python 2.6+ for this module.')

__all__ = [
    'litenc_lxml'
]