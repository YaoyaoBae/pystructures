from setuptools import setup

setup(name='pystructures',
      version='0.1',
      description='Implementation of Trees in Python',
      long_description='None',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Data Structures :: Trees',
      ],
      keywords='Data structures algorithms python',
      url='http://github.com/hturner08/pystructures',
      author='Herbert Turner',
      author_email='hturner@andover.edu',
      license='MIT',
      packages=['pystructures'],
      install_requires=[
          'coverage==4.0.1',
          'pytest==3.4.1',
          'setuptools==36.0.1',
          'attrs==17.4.0',
          'six==1.10.0',
          'colorama==0.3.9',
          'pluggy==0.6.0',
          'py==1.5.2',
      ],
      include_package_data=True,
      zip_safe=False)
