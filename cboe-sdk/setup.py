from runpy import run_path
from pathlib import Path
from setuptools import find_namespace_packages, setup


package_name = "cboe-pitch"

install_deps = ["pydantic", "boltons", "xotl.tools", "parse"]
setup_deps = []
test_deps = []
extra_deps = {}
entry_points = {}


# Don't touch the rest please, should be same across packages

# real setup.py shouldn't use Path in case someone tries to pip install with python2
THIS_DIR = Path(__file__).resolve().parent


def get_about(package_name):
    pkg_dir = THIS_DIR / package_name.replace("-", "/")
    return run_path(str(pkg_dir / "__about__.py"))


about = get_about(package_name)

setup(
    name=package_name,
    version=about["__version__"],
    packages=find_namespace_packages(include="cboe.*"),
    # package_dir={"": "src"},
    zip_safe=False,
    install_requires=install_deps,
    setup_requires=setup_deps,
    tests_require=test_deps,
    extras_require=extra_deps,
    entry_points=entry_points,
)

