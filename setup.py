from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as README:
    long_description = README.read()

version = '1.2'

setup(
    name='minehut',
    version=version,
    author='SuperOrca',
    description='Minehut API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SuperOrca/minehut-api',
    packages=find_packages(),
    install_requires=[
        'requests',
        'asyncio',
        'pyppeteer',
        'DateTime'
    ],
    classfiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
