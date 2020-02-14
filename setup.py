import ksoftapi

from setuptools import setup


def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


version = ksoftapi.__version__

if not version:
    raise RuntimeError('Version is not set')

with open('README.md') as f:
    readme = f.read()

setup(
    name='ksoftapi',
    packages=['ksoftapi'],
    version=version,
    description='KSoft.Si API Wrapper, customised for use in discord.py',
    long_description=readme,
    author='AndyTempel',
    author_email='support@ksoft.si',
    url='https://github.com/KSoft-Si/ksoftapi.py',
    download_url=f'https://github.com/KSoft-Si/ksoftapi.py/archive/{version}.tar.gz',
    keywords=['ksoftapi'],
    include_package_data=True,
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
