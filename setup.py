import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

PY3 = sys.version_info[0] == 3

requires = [
    'pyramid',
    'WebTest',
    'robotsuite',
    'robotframework-selenium2library',
    'decorator',
    'selenium'
]

if PY3:
    requires.append('robotframework-python3')
else:
    requires.append('robotframework')

setup(name='pyramid_robot',
      version='1.1',
      description='Convenience package for enable RobotFramework tests under Pyramid.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Victor Fernandez de Alba',
      author_email='sneridagh@gmail.com',
      url='https://github.com/sneridagh/pyramid_robot',
      keywords='web pyramid pylons test robotframework robot selenium',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_robot",
      entry_points="""
      """,
      )
