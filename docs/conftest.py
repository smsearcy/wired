import sys
from doctest import ELLIPSIS

from sybil import Sybil
from sybil.parsers.codeblock import CodeBlockParser
from sybil.parsers.doctest import DocTestParser, FIX_BYTE_UNICODE_REPR
from sybil.parsers.skip import skip

if sys.version_info >= (3, 7):
    pytest_collect_file = Sybil(
        parsers=[
            DocTestParser(optionflags=ELLIPSIS | FIX_BYTE_UNICODE_REPR),
            CodeBlockParser(future_imports=['print_function']),
            skip
        ],
        pattern='index.rst',
        excludes=['docs/tutorials/dcdi/* ']
    ).pytest()
