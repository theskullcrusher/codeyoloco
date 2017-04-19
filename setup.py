from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('codeyoloco.egg-info/requires.txt') as f:
        requires = f.read().splitlines()
        
with open('VERSION') as f:
    version = f.read().strip()

setup(
      name = "codeyoloco",
      version = version,
      packages = find_packages(),
      package_dir = {'codeyoloco':'codeyoloco'},
      author = 'codeyoloco',
      author_email = 'surajshah525@gmail.com',
      description = 'iCTF and Project Package',
      license = "PSF",
      include_package_data = True,
      ) 
