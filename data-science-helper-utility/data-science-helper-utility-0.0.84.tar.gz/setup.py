# -*- coding: utf-8 -*-
"""ejemplo_paquete module can be installed and configured from here"""



import json
from os import path
from setuptools import setup, find_packages
from sys import version_info


VERSION = "0.0.84"
CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')



def path_format(file_path=None, file_name=None, is_abspath=False,
                ignore_raises=False):
    """
    Get path joined checking before if path and filepath exist,
     if not, raise an Exception
     if ignore_raise it's enabled, then file_path must include '/' at end lane
    """
    path_formatted = "{}{}".format(file_path, file_name)
    if ignore_raises:
        return path_formatted
    if file_path is None or not path.exists(file_path):
        raise IOError("Path '{}' doesn't exists".format(file_path))
    if file_name is None or not path.exists(path_formatted):
        raise IOError(
            "File '{}{}' doesn't exists".format(file_path, file_name))
    if is_abspath:
        return path.abspath(path.join(file_path, file_name))
    else:
        return path.join(file_path, file_name)


def read_file(is_json=False, file_path=None, encoding='utf-8',
              is_encoding=True, ignore_raises=False):
    """Returns file object from file_path,
       compatible with all py versiones
    optionals:
      can be use to return dict from json path
      can modify encoding used to obtain file
    """
    text = None
    try:
        if file_path is None:
            raise Exception("File path received it's None")
        if version_info.major >= 3:
            if not is_encoding:
                encoding = None
            with open(file_path, encoding=encoding) as buff:
                text = buff.read()
        if version_info.major <= 2:
            with open(file_path) as buff:
                if is_encoding:
                    text = buff.read().decode(encoding)
                else:
                    text = buff.read()
        if is_json:
            return json.loads(text)
    except Exception as err:
        if not ignore_raises:
            raise Exception(err)
    return text


def read(file_name=None, is_encoding=True, ignore_raises=False):
    """Read file"""
    if file_name is None:
        raise Exception("File name not provided")
    if ignore_raises:
        try:
            return read_file(
                is_encoding=is_encoding,
                file_path=path_format(
                    file_path=CURR_PATH,
                    file_name=file_name,
                    ignore_raises=ignore_raises))
        except Exception:
            # TODO: not silence like this,
            # must be on setup.cfg, README path
            return 'NOTFOUND'
    return read_file(is_encoding=is_encoding,
                     file_path=path_format(
                         file_path=CURR_PATH,
                         file_name=file_name,
                         ignore_raises=ignore_raises))


setup(
    name='data-science-helper-utility',
    version=VERSION,
    license=read("LICENSE", is_encoding=False, ignore_raises=True),
    packages=find_packages(),
    description='data-science-helper de proyectos de analitica avanzada',
    long_description=read("README.md"),
    author='Analitica Avanzada',
    author_email='analitica.avanzada.talento@gmail.com',
    
    download_url='https://URL_PAQUETE/data-science-helper-utility/-/archive/master/data-science-helper-utility-master.tar'.format(
        VERSION),
    keywords=['data-science-helper-utility','ds-helper','paquete','package'],
    install_requires=[
        'pandas==1.2.2',
        'numpy==1.19.2',
        'plotly==4.3.0',
        'seaborn==0.9.0',
        'scikit-learn==0.23.2',
        'scikit-plot==0.3.7',
        'pyodbc==4.0.30',
        'missingno==0.4.2',
        'nltk==3.4.5',
        'shap==0.38.1',
        'wordcloud==1.6.0',
        'lightgbm==3.3.2',
        'imbalanced-learn==0.8.0',
        'requests==2.27.1',
        'optuna==2.4.0'
    ],
    #setup_requires=['requests','pandas','seaborn','numpy','scikit-learn','matplotlib'],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-html',
        'pytest-dependency',
    ],    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.7',
    ],
)