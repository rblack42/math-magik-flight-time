all:	docs

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install -U pip
	pip install -r requirements.txt

.PHONY: docs
docs:
	cd src && \
		sphinx-build -b html -d _build/doctrees . ../docs

.phony: build
build:
	cd src && \
		latexmk


.phony: clean
clean:
	cd src && \
		latexmk -C && \
		rm -f *.fls *.bbl *.out *.pytxcode pythontex*
