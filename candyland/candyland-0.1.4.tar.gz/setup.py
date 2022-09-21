# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['candyland',
 'candyland.actors',
 'candyland.actors.compile',
 'candyland.actors.manage',
 'candyland.actors.parse',
 'candyland.actors.storj',
 'candyland.actors.transact',
 'candyland.components',
 'candyland.components.messages',
 'candyland.components.pipelines',
 'candyland.core',
 'candyland.core.utils',
 'candyland.data',
 'candyland.data.models',
 'candyland.data.proofs',
 'candyland.data.schemas']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'candyland',
    'version': '0.1.4',
    'description': '',
    'long_description': '',
    'author': 'FL03',
    'author_email': 'jo3mccain@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
