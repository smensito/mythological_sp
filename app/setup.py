from setuptools import setup, find_packages

setup(name='app',
      version='0.1',
      description='Flask API for vehicle data',
      url='',
      author='Alberto Niironen Orduña',
      author_email='',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['flask', 'config'])
