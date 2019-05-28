from setuptools import setup, find_packages


setup(
    name='mp_utils',
    version="0.5",
    description='python3 utils for multiprocessing',
    author = 'Tim Olson',
    author_email = 'timjolson@user.noreplay.github.com',
    packages=find_packages(),
    tests_require=['pytest'],
)