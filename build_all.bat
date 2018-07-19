@echo off

python setup.py sdist
python setup.py bdist_egg
python setup.py bdist_wheel
