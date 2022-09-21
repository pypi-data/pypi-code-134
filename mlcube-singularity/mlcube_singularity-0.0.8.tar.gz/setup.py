from setuptools import find_packages, setup, Command
import os

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)


class Clean(Command):
    """Custom clean command."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.egg-info')


def schemas():
    paths = []
    for (path, _, filenames) in os.walk("mlcube_singularity/"):
        for filename in filenames:
            if filename.endswith(".yaml"):
                paths.append(os.path.join("..", path, filename))
    return paths


extra_files = schemas()


setup(
    name="mlcube_singularity",
    version="0.0.8",
    packages=find_packages(exclude=["tests"]),
    license="Apache 2.0",
    entry_points='''
        [console_scripts]
        mlcube_singularity=mlcube_singularity.__main__:cli
    ''',
    install_requires=requires,
    python_requires='>=3.6',
    package_data={"": extra_files},
    extras_require={},
    cmdclass={
        'clean': Clean,
    },
    long_description="MLCube Singularity runner.",
    long_description_content_type="text/markdown",
)
