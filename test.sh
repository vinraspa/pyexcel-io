pip freeze
nosetests --with-coverage --cover-package pyexcel_io --cover-package tests --with-doctest --doctest-extension=.rst README.rst docs/source pyexcel_io && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
