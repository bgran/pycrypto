tests:
	python3 -m unittest test_rsa.py
pylint:
	pylint3 --disable=invalid-name,too-few-public-methods,fixme,line-too-long,unneeded-not,no-else-return,too-many-instance-attributes rsa.py
