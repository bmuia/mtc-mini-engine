from setuptools import setup, find_packages

setup(
    name='zapper_cli',
    version='0.0.1',
    description='An authentication mini engine',
    author='Belam Muia',
    packages=find_packages(),
    install_requires=[
        'click',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'zipp=terminal.cli:cli'
        ]
    },
    python_requires='>=3.10'
)
