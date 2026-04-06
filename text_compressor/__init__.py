"""
text-compressor - Compress text while preserving meaning

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import TextCompressor, compress, process, main

__all__ = ["TextCompressor", "compress", "process", "main"]
