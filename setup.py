from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in libmanagement/__init__.py
from libmanagement import __version__ as version

setup(
	name="libmanagement",
	version=version,
	description="Library Management System",
	author="Baljit Singh",
	author_email="balsehra445@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
