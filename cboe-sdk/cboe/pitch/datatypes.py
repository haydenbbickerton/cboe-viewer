from functools import partial

from pydantic import Schema, constr

import cboe.pitch.validators as validators

# MsgType = constr(regex=ALPHA_RE)
PrintableAscii = constr(regex=validators.PRINTABLE_RE)
Alpha = constr(regex=validators.ALPHA_RE)
Numeric = constr(regex=validators.NUMERIC_RE)
Base36Numeric = constr(regex=validators.BASE36_NUMERIC_RE)
Price = constr(regex=validators.PRICE_RE)
Timestamp = constr(regex=validators.TIMESTAMP_RE)


def MsgType(name, **kwargs):
    # Camelcase because these return constructed classes
    return constr(regex=f"^{name}$", **kwargs)


def OneOf(*names, **kwargs):
    # Also allow a space, for empty field value
    names = "|".join(["\x20", *names])
    return constr(regex=f"^{names}$", **kwargs)


OrderSide = OneOf("B", "S")
