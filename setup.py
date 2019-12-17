from setuptools import setup

from aida import name, version

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name=name,
    version=version,
    author="Sevak Harutyunyan",
    author_email="sevak.g.harutyunyan@gmail.com",
    install_requires=install_requires
)
