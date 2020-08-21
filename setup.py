import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_background_task",
    version="0.1.0",
    author="fallthrough",
    author_email="rainbroadcast@gmail.com",
    description="A background task base on thread,easy to integer with any framework",
    url="https://github.com/igzhang/simple_background_task.git",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
    ]
)
