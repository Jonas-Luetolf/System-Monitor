compile:
	python3.10 setup.py bdist
	mv dist/system-monitor-0.1.linux-x86_64.tar.gz system-monitor-0.1.tar.gz
	rm -r dist/
	rm -r build/
