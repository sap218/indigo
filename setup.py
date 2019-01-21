import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='indigo',
      version='0.1',
      description='Command Line to-do list',
      url='https://github.com/sap218/indigo',
      author='Samanthe C Pendleton',
      author_email='samanfapendle@outlook.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
      zip_safe=False,
      entry_points = {'console_scripts': ['indigo=indigo.indigo:main']},
      include_package_data = True
)
