from setuptools import setup
setup(
    name = 'pokedex',
    version = '0.0.1',
    packages = ['src'],
    entry_points = {
        'console_scripts': [
            'pokedex = src.__main__:main'
        ]
    }
)# 