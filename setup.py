from setuptools import setup, find_packages

setup(
    name="rfdetr",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",        # optional
    install_requires=[              # optional
        "torch>=1.13.0",
        "torchvision>=0.14.0",
        # …other deps…
    ],
    entry_points={
        "console_scripts": [
            "rfdetr=rfdetr.cli.main:trainer",
        ],
    },
    include_package_data=True,
)
