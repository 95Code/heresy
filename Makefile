# Create virtual env with python3.8
# Upgrade pip
# Create kivy.pth file to link system kivy
venv:
	python3.8 -m venv "P-<3" 
	"P-<3/bin/pip" install --upgrade pip
	echo "/usr/lib/python3.8/site-packages/kivy/" > "P-<3/lib/python3.8/site-packages/kivy.pth"

install:
	"P-<3/bin/pip" install -r requirements.txt
