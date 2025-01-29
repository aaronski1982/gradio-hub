from setuptools import setup, find_packages

setup(
    name="public_dns_tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "flask>=2.0.0",
    ],
    entry_points={
        'console_scripts': [
            'public-dns=src.cli:main',
        ],
    },
    author="Aaron Hayes",
    description="A tool for publishing and monitoring project URLs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
) 