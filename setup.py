from setuptools import setup, find_packages


setup(
    name='mp_utils',
    version="0.5",
    description='python3 utils for multiprocessing',
    author = 'timjolson',
    author_email = '5532473+timjolson@users.noreply.github.com',
    packages=find_packages(),
    tests_require=['pytest'],
)