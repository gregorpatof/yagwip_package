import setuptools

setuptools.setup(
    name="yagwip",
    version="0.1",
    author="Gregor Patof",
    description="Yet Another Gromacs Wrapper In Python",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

