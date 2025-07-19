from setuptools import setup, find_packages

setup(
    name ='document_portal',
    version='0.1.0',
    author='Rakesh Sharma',
    description='A Document management portal built with LLM',
    long_desccription=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rakuiit/document_portal',
    packages=find_packages(),
)