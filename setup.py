from datetime import datetime

from setuptools import setup, find_packages

REQUIRES = [
    "aliz-aip-token",
    "certifi",
    "python-dateutil",
    "six",
    "urllib3",
]

VERSION = "1.0." + datetime.now().strftime("%Y%m%d")
DESCRIPTION = "Aliz AIP SDK"
DESCRIPTION_DETAILS = "An API SDK for Aliz AIP"

setup(
    name="aliz-aip-sdk",
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION + DESCRIPTION_DETAILS,
    author_email="aip-support@aliz.ai",
    install_requires=REQUIRES,
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={
        "": ["*.py"],
    },
    entry_points={
        "console_scripts": [],
    },
)
