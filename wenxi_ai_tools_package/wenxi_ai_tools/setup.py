from setuptools import setup, find_packages

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="wenxi-ai-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    entry_points={
        "console_scripts": [
            "wenxi-ai-tools = wenxi_ai_tools.main:run",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)

setup(
    name="wenxi-csv-app",
    version="0.1.0",
    packages=find_packages(),

    install_requires=[
        "pandas",
        "openpyxl"
    ],

    entry_points={
        "console_scripts": [
            "wenxi-csv-app = wenxi_csv_app.main:run",
        ],
    },

    long_description=description,
    long_description_content_type="text/markdown",
)
