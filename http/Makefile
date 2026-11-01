# http: standalone single-header HTTP/WebSocket + TCP server/client
# library (http.h). No dependency on any other repo -- just libc and
# OpenSSL (for the SHA1 used by the WebSocket handshake).
#
# Usage:
#   make test    # build + run test_http

BLD_DIR := build

CC := clang
BUILD_TYPE := debug

CFLAGS := -std=c99 \
	-D_POSIX_C_SOURCE=200809L \
	-D_GNU_SOURCE \
	-Wall \
	-Wpedantic \
	-Wno-deprecated-declarations \
	-ggdb

ifeq ($(BUILD_TYPE), debug)
	CFLAGS += -g -fsanitize=address -static-libsan
else
	CFLAGS += -g -O3 -march=native -DNDEBUG
endif

LDFLAGS := -ggdb -lssl -lcrypto

.PHONY: help
help: ## List make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile \
		| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[1;34m%-12s\033[0m%s\n", $$1, $$2}'

$(BLD_DIR):
	@mkdir -p $(BLD_DIR)

$(BLD_DIR)/test_http: test_http.c http.h | $(BLD_DIR)
	@echo "TEST [test_http]"
	@$(CC) $(CFLAGS) test_http.c -o $@ $(LDFLAGS)

.PHONY: test
test: $(BLD_DIR)/test_http ## Build and run test_http
	@$(BLD_DIR)/test_http

.PHONY: cppcheck
cppcheck: ## Run cppcheck
	@cppcheck http.h

.PHONY: clean
clean: ## Clean build output
	@rm -rf $(BLD_DIR)
