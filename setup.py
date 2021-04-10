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
    url='https://github.com/SuperOrca/minehut-api',
    packages=setuptools.find_packages(),
    classfiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
