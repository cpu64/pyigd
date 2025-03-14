from setuptools import setup, find_packages


def requirements() -> list:
    return [
        'click==8.1.8',
        'curio-compat==1.6.7',
        'requests==2.32.3',
        'yarl==1.18.3',
        'lxml==5.3.1',
        'beautifulsoup4==4.13.3',
        'tabulate==0.9.0',
    ]


setup(
    name='igd',
    version='0.1.1',
    description='IGD management CLI tool.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/pyigd',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    entry_points={
        'console_scripts': ['igd = igd.__main__:main']
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Topic :: System :: Networking',
    ],
    install_requires=requirements(),
)
