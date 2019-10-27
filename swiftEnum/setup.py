import os
import re

from setuptools import find_packages
from setuptools import setup

root = os.path.dirname(__file__)

print("root", root)

with open(os.path.join(root, "VERSION"), "rt", encoding="utf8") as f:
    version = f.read().strip()

with open(os.path.join(root, "README.md"), "rt", encoding="utf8") as f:
    long_description = f.read().strip()

setup(
    name='swiftEnum',
    version=version,
    long_description=long_description,
    license="BSD",
    packages=find_packages(),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False
)
