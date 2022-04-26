from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='DescriptiveTester',
    version='0.0.1',
    description='Descriptive Testing Utilities for Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Jay Shukla',
    author_email='jshukla@infosenseglobal.com',
    keywords=['Testing', 'Descriptive Testing', 'Excel Testing'],
    # url='https://github.com/ncthuc/elastictools',
    # download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'pandas'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)