# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rcds',
 'rcds.backend',
 'rcds.backends',
 'rcds.backends.k8s',
 'rcds.backends.rctf',
 'rcds.challenge',
 'rcds.cli',
 'rcds.project',
 'rcds.util']

package_data = \
{'': ['*'], 'rcds.backends.k8s': ['templates/*']}

install_requires = \
['Jinja2>=2.11.2,<3.0.0',
 'click>=7.1.2,<8.0.0',
 'docker>=4.3.1,<5.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'kubernetes>=12.0.0,<13.0.0',
 'pathspec>=0.8.1,<0.9.0',
 'pyyaml>=5.3.1,<6.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.24.0,<3.0.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.9'],
 'docs': ['sphinx>=3.3.0,<4.0.0',
          'sphinx_rtd_theme>=0.5.0,<0.6.0',
          'sphinx-jsonschema>=1.15,<2.0']}

entry_points = \
{'console_scripts': ['rcds = rcds.cli:cli']}

setup_kwargs = {
    'name': 'rcds',
    'version': '0.1.4',
    'description': 'An automated CTF challenge deployment tool',
    'long_description': "#######\nrCDS\n#######\n\n.. image:: https://github.com/redpwn/rCDS/workflows/CI/badge.svg\n    :target: https://github.com/redpwn/rCDS/actions?query=workflow%3ACI+branch%3Amaster\n    :alt: CI Status\n\n.. image:: https://img.shields.io/codecov/c/gh/redpwn/rcds\n    :target: https://codecov.io/gh/redpwn/rcds\n    :alt: Coverage\n\n.. image:: https://img.shields.io/readthedocs/rcds/latest\n    :target: https://rcds.redpwn.net/\n    :alt: Docs\n\n.. image:: https://img.shields.io/pypi/v/rcds\n    :target: https://pypi.org/project/rcds/\n    :alt: PyPI\n\n.. This text is copied from the first paragraphs of doc/index.rst\n\nrCDS is redpwn_'s CTF challenge deployment tool. It is designed to automate the\nentire challenge deployment process, taking sources from challenge authors and\nprovisioning the necessary resources to both make challenges available on the\ncompetition scoreboard and to spin up Docker containers that the challenge needs\nto run.\n\nrCDS has an opinionated model for managing CTF challenges. It operates on a\ncentralized challenge repository and is designed to be run from a CI/CD system.\nThis repository is the single source of truth for all data about challenges, and\nrCDS itself essentially acts as a tool to sync the state of various systems (the\nscoreboard and the container runtime) to what is described by this repository.\nAuthors do not directly interface with any of these systems, and instead push\ntheir changes and let a CI job apply them. Thus, the challenge repository can be\nversioned, creating an audit log of all changes and allowing for point-in-time\nrollbacks of everything regarding a challenge should something go wrong.\n\nFor more information, see `the documentation <https://rcds.redpwn.net/>`_.\n\n.. _redpwn: https://redpwn.net/\n",
    'author': 'redpwn',
    'author_email': 'contact@redpwn.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rcds.redpwn.net',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
