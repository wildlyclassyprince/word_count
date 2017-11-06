from setuptools import setup

setup(
    name='word_count',
    entry_points={
        'console_scripts':['word_count=word_count:main',],
    },
    author = 'wildlyclassyprince',
    author_email = 'lihtumb@gmail.com',
    url = 'https://github.com/wildyclassyprince/word_count'
)
