import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danbot-status", # Replace with your own username
    version="0.2.1",
    author="VineyS",
    author_email="vineypsunu@gmail.com",
    description="Status Of All Services of DanBotHost(DBH)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VineyS/danbot-status-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["aiohttp>=3.6.0,<3.8.0", "requests>=2.22.0,<3.0.0"],
    python_requires='>=3.6',
)
