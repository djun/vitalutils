import setuptools
 
setuptools.setup(
    name="vitaldb",
    version="0.1.19",
    author="Hyung-Chul Lee",
    author_email="vital@snu.ac.kr",
    description="VitalDB Python Libray",
    long_description="VitalDB Python Libray",
    long_description_content_type="text/markdown",
    url="https://github.com/vitaldb/vitalutils",
    install_requires=['numpy', 'pandas', 'requests', 's3fs', 'pyarrow'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)