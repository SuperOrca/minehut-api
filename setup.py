import setuptools

with open('README.md', 'r', encoding='utf-8') as README:
    long_description = README.read()

setuptools.setup(
    name='minehut',
    version='1.0.0',
    author='SuperOrca',
    description='Minehut API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SuperOrca/minehut',
    packages=setuptools.find_packages(),
    classfiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2.25.1', 'asyncio>=3.4.3', 'pyppeteer>=0.2.5', 'DateTime>=4.3']
)
