from setuptools import setup, find_packages

setup(
    name='bosonpy', 
    version='1.0.0', 
    packages=['bosonpy'],
    author="Zac Pullen",
    email="zac@greenroomrobotics.com",
    install_requires=["pyserial", "pyudev", "numpy"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    )
