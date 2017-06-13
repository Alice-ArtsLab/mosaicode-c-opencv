# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: C',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='mosaicode_c_opencv',
      install_requires=['Python>=2.7'],
      tests_require=[],
      test_suite='',
      version='1.0',
      packages=[
          'mosaicode_c_opencv',
          'mosaicode_c_opencv.opencv',
          'mosaicode_c_opencv.ports'],
      scripts=[],
      description='Image Processing and Computer Vision \
      Automatic Programming Tool',
      author='Ouroboros',
      author_email='',
      maintainer="Ouroboros",
      maintainer_email="",
      license="GNU GPL3",
      url='http://ges.dcomp.ufsj.edu.br/index.php/ouroboros/',

      # this is fucked up! must put it in package_data!!
      data_files=[],
      **config
      )
