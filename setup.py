from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operation System :: GNU/Linux",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python :: 3.9.9",
]

setup(
    name="xhibit",
    version="0.0.1",
    description="A python script to exhibit your ascii arts and sytem specs",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="git clone https://github.com/glowfi/xhibit",
    author="glowfi",
    author_email="",
    license="GPLv3+",
    classifiers=classifiers,
    keywords="system-information ascii-art",
    packages=find_packages(),
    install_requires=["tcolorpy"],
)
