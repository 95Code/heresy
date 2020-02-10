# Create virtual env with python3.8
# Upgrade pip
# Create kivy.pth file to link system kivy
venv:
	python3.8 -m venv venv
	venv/bin/pip install --upgrade pip
	echo "/usr/lib/python3.8/site-packages/kivy/" > venv/lib/python3.8/site-packages/kivy.pth

install:
	venv/bin/pip install -r requirements.txt
