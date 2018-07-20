from setuptools import setup

dependencies = [
    "xlrd>=1.1.0",
    "requests>=2.19.1",
    "flask>=0.12.2"
]

setup(
    name="Work Applications Bot",
    version="0.99",
    description="library for automatically sending job applications via StackOverflow",
    url='https://github.com/myusuf3/delorean',
    author='Rafael Marques',
    author_email="rafaelmarques76076@gmail.com",
    keywords="stackoverflow jobs automation",
    packages=['jobs'],
    scripts=["autojob"],
    license='MIT license',
    install_requires=dependencies,
    test_suite='tests.main_test',
    long_description=open('README.md').read(),
)