# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telescope_sdk']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses_json>=0.5.7,<0.6.0',
 'flake8>=5.0,<6.0',
 'pycountry>=22.3.5,<23.0.0']

setup_kwargs = {
    'name': 'telescope-sdk',
    'version': '0.0.1',
    'description': 'Telescope Python SDK',
    'long_description': '# Telescope Python SDK\n\nPackage containing Python dataclasses representing the entities used in Telescope backend systems. The source of truth\nfor these types lives [here](https://gotelescope.atlassian.net/wiki/spaces/~62cc5da0bb346bdf82fa14f7/pages/32899073/Data+model+changes+move+to+Person).\n\nSee [Deployment](#deployment) for instructions on how to publish a new version of this package.\n\n\n## Development\n\nTo make changes to this package clone the repo and follow the steps below. Please ensure that any changes to the code\nbase are synced with the documentation linked above.\n\n### Installation\n\nFirst set up a virtual environment to isolate dependencies. You can do this in many ways but as an example:\n\n```bash\n$ pyenv virtualenv 3.10.0 <chosen-virtualenv-name>\n$ pyenv activate <chosen-virtualenv-name>\n```\n\nNote this codebase takes advantage of features from Python 3.10+ therefore you may run into errors if you attempt to use\nan earlier Python version.\n\nThis project relies on Poetry for dependency management. To install Poetry follow the instructions\n[here](https://python-poetry.org/docs/#installing-with-pipx) (recommend using [pipx](https://pypa.github.io/pipx/) to\ninstall Poetry globally but manage in virtualenv).\n\nNow ensure you have Make on your machine then run\n\n```bash\n$ make install\n```\n\nThis will install the package and its dependencies in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).\n\n### Testing\n\nTo run tests locally, run the following command:\n\n```bash\n$ make test\n```\n\n### Linting\n\nTo run linting locally, run the following command:\n\n```bash\n$ make lint\n```\n\n## Deployment\n\nA new package version is published to PyPI whenever a new release is created on GitHub. To create a new release follow\nthe following steps, from the `master` branch:\n\n1. Update the version number in `pyproject.toml` to the new version number (use semantic versioning).\n2. Create a new release on GitHub with the same version number as the one in `pyproject.toml`.\n3. Draft release notes for the new version. These will be used as the package description on PyPI.\n4. The new version will be published to [PyPI](https://pypi.org/) automatically.\n\nOn pushes to the `master` branch, the `sandbox-deploy` job will run and publish a new version of the package to\n[TestPyPI](https://test.pypi.org/). This is useful for testing changes to the package before publishing to PyPI.\n',
    'author': 'Camin McCluskey',
    'author_email': 'camin@gotelescope.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/telescope-eng/telescope-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
