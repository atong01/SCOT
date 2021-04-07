from setuptools import find_packages, setup

install_requires = [
    "POT",
    "sklearn",
    "scipy",
    "numpy",
    "torch",
    "git+https://github.com/atong01/unbalanced_gromov_wasserstein",
]

setup(
    name="SCOT",
    version="0.2.1",
    description="Gromov-Wasserstein optimal transport for aligning single-cell multi-omics data",
    author="Pinar Demetci",
    packages=find_packages(),
    license="MIT",
    install_requires=install_requires,
)
