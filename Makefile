VENV = "P-\<3"
PIP = "$(VENV)/bin/pip" 
PY = "$(VENV)/bin/python" 

venv:
	python3.8 -m venv $(VENV) 
	$(PIP) install --upgrade pip
	$(PIP) install cython 

install:
	$(PIP) install -r requirements.txt

clean:
	rm -rf $(VENV)
