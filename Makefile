compile:
	python3.10 setup.py bdist
	mv dist/system-monitor-1.0.linux-x86_64.tar.gz system-monitor-1.0.tar.gz
	rm -r dist/
	rm -r build/
