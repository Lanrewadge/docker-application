from setuptools import setup, find_packages
import shutil

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='myapp',
    version='1.0.0',
    author='Toluwalase Adedotun',
    author_email='toluadedotun@gmail.com',
    description='A brief description of your application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cloudboostauk/python-CI-CD-with-Jenkins-and-ArgoCD',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'myapp=main:main'
        ]
    },
    install_requires=install_requires
)

# Rename the folder
shutil.move('dist/myapp-1.0.0-py3-none-any.whl', 'dist/myapp-1.0.0-py3-none-any.dist-info')
