.PHONY: docs

help:
	@echo "\033[1;34m[make targets]:\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[1;36m%-12s\033[0m%s\n", $$1, $$2}'

docs: ## Docs
	@sleep 3 && xdg-open http://127.0.0.1:8000 &
	@rm -rf docs/build
	@pip install sphinx
	@pip install sphinx-rtd-theme
	@pip install sphinxcontrib-napoleon
	@pip install sphinx-hoverxref
	@pip install sphinxcontrib-bibtex
	@sphinx-autobuild docs/source docs/build/html
