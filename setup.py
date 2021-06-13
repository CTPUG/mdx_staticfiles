from setuptools import setup

REQUIRES = [
    "Django",
    "markdown",
]

SOURCES = []

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name="mdx-staticfiles",
    version="0.1",
    url="http://github.com/CTPUG/mdx_staticfiles",
    license="MIT",
    description="A django.contrib.staticfiles extension for Markdown",
    long_description=long_description,
    author="CTPUG",
    author_email="ctpug@googlegroups.com",
    py_modules=["mdx_staticfiles"],
    install_requires=REQUIRES,
    dependency_links=SOURCES,
    setup_requires=[
        # Add setuptools-git, so we get correct behaviour for
        # include_package_data
        "setuptools_git >= 1.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
