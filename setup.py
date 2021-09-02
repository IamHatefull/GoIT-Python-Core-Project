from setuptools import setup, find_packages


setup(
    name="Assistant",
    version="1.0",
    description='Assistant bot cli',
    url='https://github.com/Bohdan-developer/GoIT-Python-Core-Project/blob/master/Assistant/',
    author='Bohdan Kostenko, Dmytro Kocherha, Vladimir Voitov, Boris Denisenko',
    author_email='bohdan.kostenko2020@gmail.com, baksy933@gmail.com, dm.kocherha@gmail.com, borysman3@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['Assistant=Assistant.main:main']}
)