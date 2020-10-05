from setuptools import setup, find_packages
setup(
    name = "CrossQuantilogram",
    author = "Yisong WANG",
    author_email = "richardwang96@qq.com",
    url = "https://github.com/wangys96/Cross-Quantilogram",
    description = "Python3 implementation of Cross-Quantilogram statistics and analysis",
    version = "0.0.2",
    license = "MIT",

    packages = find_packages("src"),
    package_dir = {'':'src'}, 

    python_requires = '>=3',
    install_requires = [
        'numpy>=1.16.0',
        "pandas>=0.23.0",
        "statsmodels>=0.9.0",
        "matplotlib>=3.0.2"
        ],

    classifiers = [
    # How mature is this project? Common values are
    # 3 - Alpha
    # 4 - Beta
    # 5 - Production/Stable
    "Development Status :: 5 - Production/Stable",

    # Indicate who your project is intended for
    "Intended Audience :: Science/Research",

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    ],
)