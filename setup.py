from setuptools import setup, find_packages

setup(
    name="omv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "platformdirs",  # Dependencia externa necesaria
    ],
    entry_points={
        "console_scripts": [
            "omv = omv.main:main",  # Comando CLI para ejecutar tu aplicación
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versión mínima de Python requerida
)