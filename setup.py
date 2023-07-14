import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xhibit",
    version="9.7.0",
    author="glowfi",
    description="A python script to exhibit your ascii arts and sytem specs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/glowfi/xhibit",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "xhibit=Exhibition.__init__:__init__",
        ]
    },
    install_requires=["tcolorpy"],
    scripts=["./Exhibition/pos.sh", "./Exhibition/shell.sh"],
)
