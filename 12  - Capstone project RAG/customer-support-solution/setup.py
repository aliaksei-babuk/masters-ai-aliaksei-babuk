from setuptools import setup, find_packages

setup(
    name="customer-support-solution",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A customer support solution that answers questions and raises support tickets.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/customer-support-solution",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit",
        "gradio",
        "requests",
        "faiss-cpu",
        "PyPDF2",
        "langchain",
        "openai",
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)