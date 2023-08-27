"""
Setup file for churn_prediction_aws package
Latest update: 2023-08-27
"""


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "churn_prediction_aws"
AUTHOR_NAME = "RThaweewat"
AUTHOR_EMAIL = "thaweewat.data@gmail.com"
SRC_REPO = "churn_prediction"


setuptools.setup(
	name=REPO_NAME,
	version=__version__,
	author=AUTHOR_NAME,
	author_email=AUTHOR_EMAIL,
	description="Churn prediction module",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
	project_urls={
		"Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
	},
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src")
)


