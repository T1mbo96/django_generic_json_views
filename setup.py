from setuptools import find_packages, setup

setup(
    name='django_generic_json_views',
    packages=find_packages(include=['django_generic_json_views']),
    version='0.1.0',
    description='Generic JSON class based views for the webframework Django.',
    author='Timo Michel',
    license='MIT',
    install_requires=['Django==3.2.9'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.5'],
    test_suite='tests'
)