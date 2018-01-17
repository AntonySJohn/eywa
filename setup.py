from setuptools import setup
from setuptools import find_packages
import os


install_requires = ['numpy', 'dateparser', 'mkdocs', 'mkdocs-material']
dependency_links = []

if os.name == 'nt':
      os.system('python -m easy_install annoy-1.8.0-py2.7-win-amd64.egg')
else:
      dependency_links.append("git+ssh://git@github.com/farizrahman4u/annoy.git")

setup(
      name='eywa',
      version='0.0.1',
      description='Language Understanding Engine',
      author='Fariz Rahman',
      author_email='fariz@datalog.ai',
      url='https://github.com/farizrahman4u/lue',
      license='GNU GPL v2',
      install_requires=install_requires,
      dependency_links=dependency_links,
      packages=find_packages(),
      include_package_data=True
)
