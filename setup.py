from setuptools import setup, find_namespace_packages

setup(
    name='sorts_files',
    version='1.0',
    description='This program sorts files in the selected folder',
    url='https://github.com/AntonSokhnenko/clean_folder.git',
    author='Sokhnenko Anton',
    author_email='ant.sokhnenko@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={"console_scripts": ["clean_folder=clean_folder.clean:sort_file"]}
    )
