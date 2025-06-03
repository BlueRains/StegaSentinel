init:
	pip install -r requirements.txt
test:
	py.test tests

doc:
	pdoc src --docformat=google
format:
	ruff format
	ruff check
.PHONY: init test doc format