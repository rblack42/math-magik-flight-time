all:	docs

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install -U pip
	pip install -r requirements.txt

.phony: pdf
pdf:
	cd tex && \
		latexmk


.phony: clean
clean:
	cd tex && \
		latexmk -C && \
		rm -f *.fls *.bbl *.out *.pytxcode pythontex*

.PHONY: docs
docs:
	jupyter-book build article/
	cp -R article/_build/html/ docs

.PHONY: nb
nb:
	cd article && \
		jupyter notebook
