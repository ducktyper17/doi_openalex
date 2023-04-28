"""
Setup script for pkg package.
"""

from setuptools import setup

setup(name='openalex',
      version='0.0.1',
      description='bibtex and ris utilities',
      maintainer='saaksshi',
      maintainer_email='sjilhewa@andrew.cmu.edu',
      license='MIT',
      packages=['openalex'],
      scripts=[],
      entry_points={
        "console_scripts": ["cite = openalex.cmdline:cite"]},
      long_description='''to get citations bibtex/ris''')
