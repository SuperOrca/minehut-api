import setuptools
from pip.download import PipSession
from pip.req import parse_requirements

with open('README.md', 'r', encoding='utf-8') as README:
    long_description = README.read()

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]
version = '1.0.0'

setuptools.setup(
    name='minehut',
    version=version,
    install_requires=reqs,
    include_package_data=True,
    author='SuperOrca',
    license='MIT',
    description='Minehut API wrapper',
    keywords=['minehut', 'minehut api'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SuperOrca/minehut-api',
    packages=setuptools.find_packages(),
    classfiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    python_requires='>=3.6'
)
