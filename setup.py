import re
from setuptools import setup

version = ""
with open("booru/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)


requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="booru",
    author="sinkaroid",
    author_email="anakmancasan@gmail.com",
    version=version,
    long_description=readme,
    url="https://github.com/sinkaroid/booru",
    project_urls={
        "Discord": "https://discord.gg/8wj4vM5hHM",
        "Funding": "https://paypal.me/sinkaroid",
        "Issue tracker": "https://github.com/sinkaroid/booru/issues/new/choose",
        "Documentation": "https://sinkaroid.github.io/booru",
    },
    packages=["booru", "booru.client", "booru.utils"],
    license="MIT",
    classifiers=[
        "Framework :: AsyncIO",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",
    ],
    description="Python bindings for Booru imageboards",
    include_package_data=True,
    keywords=[
        "booru",
        "library",
        "hentai",
        "gelbooru",
        "rule34",
        "safebooru",
        "xbooru",
        "tbib",
        "realbooru",
        "hypnohub",
        "danbooru",
        "atfbooru",
        "yandere",
        "konachan",
        "konachan.net",
        "lolibooru",
        "e621",
        "e926",
        "derpibooru",
        "furbooru",
        "behoimi",
        "paheal",
    ],
    install_requires=requirements,
)
