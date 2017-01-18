#-*- coding: UTF-8 -*-
""" 
Distutils setup.py configuration file.
"""

from setuptools import setup, find_packages
from os.path import dirname, join

INSTALL_REQUIRES = ['Flask', 'requests']

def read(file_name):
        return open(join(dirname(__file__), file_name)).read()

def get_pkg_name(pkg_full):
    separators = ['<', '>', '==', '!=', '<=', '>=']
    for x in separators:
        if x in pkg_full:
            return pkg_full.split(x)[0]
    else:
        return pkg_full

def generate_dependency_links(install, extra=None):
    result = []
    if len(install) > 0:
        for pkg in install:
            result.append(join(get_pkg_name(pkg)))
    if extra is not None and len(extra) > 0:
        for item in extra.keys():
            for pkg in extra[item]:
                result.append(get_pkg_name(pkg))
    return result

setup(
    name="cf-route-service",
    version="1.0",
    author="Fabien Guichard",
    author_email="fabien.guichard@orange.com",
    description="route service standard pour Cloud Foundry",
    long_description=read('README'),
    license="Apache 2.0",
    packages=find_packages(),
    scripts=[],
    data_files=[],
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    dependency_links=generate_dependency_links(INSTALL_REQUIRES),
)
