from setuptools import setup, find_packages

setup(
    name='Climate Pylot',  # Required
    version='1.0.0',  # Required
    description='A brief description of your package',  # Optional
    long_description='A longer description of your package',  # Optional
    url='https://github.com/OwenRube7/climate-pylot',  # Optional
    author='Owen Rubenis',  # Optional
    classifiers=[  # Optional
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12.1',
    ],
    keywords='sample setuptools development',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/OwenRube7/climate-pylot/issues',
        'Source': 'https://github.com/OwenRube7/climate-pylot',
    },
)