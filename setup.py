from setuptools import setup, find_packages

setup(
    name='musicfilesync',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tinytag'
    ],
    entry_points={
        'console_scripts': [
            'musicfilesync = musicfilesync.musicfilesync:main',
        ]
    }
)
