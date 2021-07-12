from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
      name='fileSizeUtils',
      version='0.0.1',
      description='File size utils contains method for conversion between size unit like byte, kilobyte, megabyte...',
      py_modules=['fileSizeUtils'],
      package_dir={'':'src'},
      long_description=long_description,
      long_description_content_type="text/markdown",
      extras_require = {
        "dev": [
            "pytest>=3.7",
        ]
      }
)