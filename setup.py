#!/usr/bin/env python3
"""
Replicate MCP - Setup Script
By Daniel Fleuren
"""

import os
from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="replicate-mcp",
    version="1.0.0",
    author="Daniel Fleuren",
    author_email="daniel@example.com",
    description="AI Media Generation for Claude Code via MCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielfleuren/replicate-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=2.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "replicate-mcp=replicate_mcp.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "replicate_mcp": ["*.json", "*.yaml", "*.yml"],
    },
    keywords="replicate mcp claude ai media generation image video audio 3d",
    project_urls={
        "Bug Reports": "https://github.com/danielfleuren/replicate-mcp/issues",
        "Source": "https://github.com/danielfleuren/replicate-mcp",
        "Documentation": "https://github.com/danielfleuren/replicate-mcp/tree/main/docs",
    },
)
