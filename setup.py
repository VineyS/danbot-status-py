import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danbot-status", # Replace with your own username
    version="0.0.1",
    author="VineyS",
    author_email="contact@roxy.host",
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
    install_requires=["requests == 2.24.0"],
    python_requires='>=3.6',
)
