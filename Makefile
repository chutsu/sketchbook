.PHONY: docs

help:
	@echo "\033[1;34m[make targets]:\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[1;36m%-12s\033[0m%s\n", $$1, $$2}'

env: ## Setup env
	@python3 -m venv venv && \
	venv/bin/pip3 install -r requirements.txt && \
	echo "Run 'source venv/bin/activate' to activate the virtualenv"

docs: ## Serve docs locally
	@echo "Open docs/index.html in your browser (e.g. python3 -m http.server 8000)"
