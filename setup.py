from setuptools import setup, find_packages

setup(
    name='Climate Pylot',
    version='1.0.0',
    description='A brief description of your package',
    long_description='A longer description of your package',
    url='https://github.com/OwenRube7/climate-pylot',
    author='Owen Rubenis',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12.1',
    ],
    keywords='sample setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/OwenRube7/climate-pylot/issues',
        'Source': 'https://github.com/OwenRube7/climate-pylot',
    },
)