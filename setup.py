import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Instructor OpenAI Embedding",
    version="0.0.1",
    author="Ching Pui WAN",
    author_email="cpwan@ust.hk",
    description="Client to call instructor model hosted in a openai-compatibale endpoint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpwan/instructor_openai_embedding",
    project_urls={
        "Bug Tracker": "https://github.com/cpwan/instructor_openai_embedding/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)