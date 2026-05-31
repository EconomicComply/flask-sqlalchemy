from _install_hook import _InstallCommand
from setuptools import setup

setup(
    cmdclass={'install': _InstallCommand},)
