import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("src/swiftEnum/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(
    name='swiftEnum',
    version=version,
    license="BSD",
    packages=find_packages(),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False
)
