from setuptools import setup


setup(name='beercaddy',
      version='0.0.1',
      description='A robot that fetches beer!',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
      ],
      keywords='raspberrypi arduino robot',
      url='https://github.com/Grungnie/beercaddy',
      author='Matthew Brown',
      author_email='mbrown1508@outlook.com',
      license='MIT',
      packages=[],
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
)