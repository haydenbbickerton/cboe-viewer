# Some YAML helpers that maintain order and don't dump weird like pyaml
import ruamel.yaml


def load(inp, **kwargs):
    return ruamel.yaml.load(inp, Loader=ruamel.yaml.RoundTripLoader, **kwargs)


def load_all(inp, **kwargs):
    return ruamel.yaml.load_all(inp, Loader=ruamel.yaml.RoundTripLoader, **kwargs)


def dump(data, stream, **kwargs):
    return ruamel.yaml.round_trip_dump(
        data,
        stream,
        indent=4,
        block_seq_indent=2,
        explicit_start=True,
        width=1000,
        **kwargs,
    )
