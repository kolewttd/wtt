from setuptools import setup, find_packages

setup(
    name='wtt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    include_package_data=True,
    description='A description of your wtt module',
    author='kolewtt',
    author_email='kolewtt@proton.me',
    url='https://github.com/kolewttd/wtt',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

