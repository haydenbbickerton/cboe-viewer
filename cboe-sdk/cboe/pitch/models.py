from functools import partial
from boltons.cacheutils import LRI, cached

from boltons.iterutils import flatten, flatten_iter
from boltons.strutils import iter_splitlines
from boltons.iterutils import bucketize

import parse
from typing import Optional, TypeVar


def parse_line(val: str):
    value = trim_starting_s(val)
    msgtypecode = value[8]
    try:
        return MESSAGE_TYPES[msgtypecode].parse_line(value)
    except KeyError as e:
        raise KeyError(f"No Message type found for: {msgtypecode}") from e


def parse_lines(lines):
    for line in filter(str.strip, lines):  # Filter out empty lines
        yield parse_line(line)


def parse_text(text):
    message_lines = iter_splitlines(text)
    yield from parse_lines(message_lines)


def group_messages(messages):
    return bucketize(messages, lambda x: x.message_type)
