from distutils.core import setup

setup(
    name='spade',
    version='0.0',
    description='Simulating PArtial Differential Equations',
    author='Arvin Kushwaha',
    author_email='arvin.singh.kushwaha@gmail.com',
    url='https://github.com/ArvinSKushwaha/SPADE/',
    packages=['spade'],
    package_dir={'spade': 'src/spade'},
    license='MIT',
    keywords=['plasma', 'laser', 'simulation'],
    long_description='This package contains tools to assist physicists in simulating complex PDE simulations. By '
                     'constructing a computational graph to represent differential equations this package allows '
                     'for great modularity and configurability in how systems are simulated.'
)
