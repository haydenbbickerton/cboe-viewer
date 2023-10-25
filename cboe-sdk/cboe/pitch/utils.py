import re
from boltons.formatutils import (
    get_format_args,
    tokenize_format_str,
    BaseFormatField,
    construct_format_field_str,
)


from boltons.cacheutils import LRI, cached
import parse


def range2chars(start: int, stop: int) -> set:
    """Get string representation of characters in given range

    Example:
        >>> # These produce identical output
        >>> range2chars(65, 90)         # Dec
        >>> range2chars(0o101, 0o132)   # Oct
        >>> range2chars(0x41, 0x5a)     # Hex
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    """
    stop += 1  # include end character
    chars = [chr(x) for x in range(start, stop)]
    return "".join(chars)


def ensure_list(v):
    return v if isinstance(v, list) else list(v)


def trim_starting_s(model, val):
    if val.startswith("S") and len(val) == (model.total_width() + 1):
        val = val[1:]
    return val


def make_fmt_str(fill=None, align=None, width=None):
    """Create a string used in the format mini specs"""
    res = ""

    if fill:
        res += fill

    if align:
        char = {"left": "<", "center": "^", "right": ">"}.get(align, align)

        res += char

    if width:
        res += str(width)

    return res


def make_named_fmt_str(name, *args, **kwargs):
    fmt_str = make_fmt_str(*args, **kwargs)
    return construct_format_field_str(name, fmt_str, None)
