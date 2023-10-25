from pathlib import Path
from typing import Dict, List, NewType

from boltons.iterutils import flatten, flatten_iter
from pydantic.dataclasses import dataclass

import lib.utils
import lib.yaml


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
            data = lib.yaml.load(file_path.read_text())
            yield from lib.utils.ensure_list(data)

    def load_specs(self):
        for spec in self.read_specs():
            data = make_pitch_model(spec)
            yield data


def load_specs_in(search_dir):
    loader = SpecLoader(search_dir)
    return loader.load_specs()


def read_specs_in(search_dir):
    loader = SpecLoader(search_dir)
    return loader.read_specs()
