from setuptools import setup

setup(
    name='word_count',
    entry_points={
        'console_scripts':['word_count=word_count:main',],
    }
)
