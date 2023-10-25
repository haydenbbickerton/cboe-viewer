from pathlib import Path
from typing import Dict, List, NewType

from boltons.iterutils import flatten, flatten_iter
from pydantic.dataclasses import dataclass
from boltons.strutils import iter_splitlines
from boltons.iterutils import bucketize

from cboe.pitch import utils, yaml


def RPath(path):
    return Path(path).resolve()


def Directory(path):
    path = RPath(path)
    return path if path.is_dir() else path.parent


def collect_files(search_path, exts: list):
    search_dir = Directory(search_path)
    for ext in flatten([exts]):
        yield from search_dir.glob(f"**/*{ext}")


@dataclass
class SpecLoader:
    search_dir: Path
    extensions = [".yml", ".yaml"]

    def read_specs(self):
        for file_path in collect_files(self.search_dir, self.extensions):
            data = yaml.load(file_path.read_text())
            yield from utils.ensure_list(data)

    def load_specs(self, loader):
        for spec in self.read_specs():
            data = loader(spec)
            yield data


def load_specs_in(search_dir, loader):
    specs = SpecLoader(search_dir)
    return specs.load_specs(loader)


def read_specs_in(search_dir):
    specs = SpecLoader(search_dir)
    return specs.read_specs()
