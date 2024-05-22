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
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/wtt',  # Update with your repo URL
    license='GPLv3',  # Specify the license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'wtt=wtt.wtt:main',  # 'wtt' is the command, 'wtt.wtt:main' points to the main function
        ],
    },
)
