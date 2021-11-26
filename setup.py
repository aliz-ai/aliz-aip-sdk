import subprocess
from datetime import datetime

from setuptools import setup, find_packages

REQUIRES = [
    "aliz-aip-token",
    "certifi",
    "python-dateutil",
    "six",
    "urllib3",
]

VERSION = "1.0"
DESCRIPTION = "Aliz AIP SDK"
DESCRIPTION_DETAILS = "An API SDK for Aliz AIP"

BUILD_DATE_FILE = ".build-date"
GIT_HASH_FILE = ".git-hash"


def get_git_revision_hash_and_build_date():
    # Try #1: if running from a git repo, get hash from rev-parse and generate GIT_HASH_FILE
    try:
        process = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = process.stdout.decode("utf-8").strip()
        if process.returncode != 0:
            raise Exception("Failed to fetch git ref from repository: {}".format(output))
        with open(GIT_HASH_FILE, "w") as f:
            f.write(output)
        build_date = datetime.now().strftime("%Y%m%d")
        with open(BUILD_DATE_FILE, "w") as f:
            f.write(build_date)
        return output, build_date
    except Exception:
        print("Executing git rev-parse failed")
    # Try #2: if running from tarball, get from included GIT_HASH_FILE generated at distribution time
    try:
        with open(GIT_HASH_FILE, "r") as f:
            git_hash = f.read().strip()
        with open(BUILD_DATE_FILE, "r") as f:
            build_date = f.read().strip()
        return git_hash, build_date
    except Exception:
        print("Git hash metadata file not found")
    # Fallback is None, we could not determine git hash
    return None, None


def format_version():
    git_hash, build_date = get_git_revision_hash_and_build_date()
    if not git_hash:
        return VERSION
    else:
        return "{}.{}+git.{}".format(VERSION, build_date, git_hash)


setup(
    name="aliz-aip-sdk",
    version=format_version(),
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
