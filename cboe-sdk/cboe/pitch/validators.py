import re


from cboe.pitch.utils import range2chars

# Regex's for use with our data types
# Also, x_CHARS for those that want to "if x in PRINTABLE_CHARS"


# Printable ASCII
# Printable ASCII values in the range of 0x20 – 0x7e
PRINTABLE_CHARS = range2chars(0x20, 0x7E)
PRINTABLE_RE = re.compile(r"^[\x20-\x7e]*$", flags=re.ASCII)

# Alpha
# Uppercase A-Z, and space(0x20)
ALPHA_CHARS = chr(0x20) + range2chars(0x41, 0x5A)
ALPHA_RE = re.compile(r"^[\x20A-Z]*$", flags=re.ASCII)

# Numeric
# ASCII numbers 0-9
NUMERIC_CHARS = range2chars(0x30, 0x39)
NUMERIC_RE = re.compile(r"^[0-9]*$", flags=re.ASCII)

# Base36 Numeric
# ASCII numbers 0-9, and Uppercase A-Z
BASE36_NUMERIC_CHARS = range2chars(0x30, 0x39) + range2chars(0x41, 0x5A)
BASE36_NUMERIC_RE = re.compile(r"^[0-9A-Z]*$", flags=re.ASCII)

# Price
# 10 ASCII numbers 0-9
PRICE_CHARS = range2chars(0x30, 0x39)
PRICE_RE = re.compile(r"^[0-9]{10}$", flags=re.ASCII)
# PRICE_RE = re.compile(r"^(?'integer'[0-9]{6})(?'fractional'[0-9]{4})$", flags=re.ASCII)

# Timestamp
# 8 ASCII numbers 0-9
TIMESTAMP_CHARS = range2chars(0x30, 0x39)
TIMESTAMP_RE = re.compile(r"^[0-9]{8}$", flags=re.ASCII)

