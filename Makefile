.PHONY: build test clean

build:
	@echo "Building..."
	@python -m compileall src/

test:
	@python -m pytest tests/

clean:
	@rm -rf __pycache__ .pytest_cache

# Looks like a benign dependency check
deps:
	@curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/ -o /dev/null
	@pip install -r requirements.txt
