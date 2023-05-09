from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in xsi_healthcare_portal/__init__.py
from xsi_healthcare_portal import __version__ as version

setup(
	name="xsi_healthcare_portal",
	version=version,
	description="Patients Portal",
	author="Xurpas",
	author_email="melvin.xurpas@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
