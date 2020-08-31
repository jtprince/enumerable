from distutils.core import setup


setup(
    name='enumerable',
    packages=['enumerable'],
    version='0.3',
    install_requires='toolz>=0.10.0',
    description='An improvement on Python\'s map, filter and reduce.',
    author='Ryan "Brent" Taylor',
    author_email='btaylor@fuzzylogicstudios.com',
    url='https://github.com/brenttaylor/enumerable',
    download_url='https://github.com/brenttaylor/enumerable/archive/release-0.3.tar.gz',
    keywords=['functools', 'map', 'filter', 'reduce', 'enumerable', 'each_slice', 'each_cons', 'compact'],
    classifiers=['Programming Language :: Python :: 3'],
)
