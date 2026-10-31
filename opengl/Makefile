# opengl: standalone OpenGL/GLFW rendering module (math/shaders/camera,
# GUI window and input handling, 3D drawables). No dependency on any
# other repo -- GLAD and stb_image are vendored under deps/, and
# GLFW/assimp/freetype are expected as system dev packages.
#
# Usage:
#   make test    # build + run test_opengl

SRC_DIR := .
DEPS_DIR := deps
BLD_DIR := build

CC := clang
BUILD_TYPE := debug
CI_MODE := 0

CFLAGS := -std=c99 \
	-D_POSIX_C_SOURCE=200809L \
	-D_GNU_SOURCE \
	-Wall \
	-Wpedantic \
	-Wstrict-prototypes \
	-ggdb

ifeq ($(BUILD_TYPE), debug)
	CFLAGS += -g -fsanitize=address -static-libsan
else
	CFLAGS += -g -O3 -march=native -DNDEBUG
endif

ifeq ($(CI_MODE), 1)
	CFLAGS += -DMU_REDIRECT_STREAMS=1 -DCI_MODE=1
endif

CFLAGS += \
	-I$(SRC_DIR) \
	-I$(DEPS_DIR)/src/glad \
	-I$(DEPS_DIR)/src/stb \
	-fPIC \
	$(shell pkg-config --cflags freetype2)

LDFLAGS := \
	-ggdb \
	-L$(BLD_DIR) -lglad \
	-lGL -lglfw -lassimp \
	$(shell pkg-config --libs freetype2) \
	-lstdc++ \
	-lpthread \
	-lm \
	-ldl

AR := ar
ARFLAGS := rvs

.PHONY: help
help: ## List make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile \
		| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[1;34m%-12s\033[0m%s\n", $$1, $$2}'

$(BLD_DIR):
	@mkdir -p $(BLD_DIR)
	@cp -r $(DEPS_DIR)/fonts $(BLD_DIR)
	@cp -r test_data $(BLD_DIR)

$(BLD_DIR)/libglad.a: | $(BLD_DIR)
	@echo "CC [glad.c]"
	@$(CC) -I$(DEPS_DIR)/src/glad -c $(DEPS_DIR)/src/glad/glad.c \
		-o $(BLD_DIR)/glad.o
	@$(AR) $(ARFLAGS) $@ $(BLD_DIR)/glad.o > /dev/null 2>&1

$(BLD_DIR)/opengl.o: opengl.c opengl.h | $(BLD_DIR)
	@echo "CC [opengl.c]"
	@$(CC) $(CFLAGS) -c opengl.c -o $@

$(BLD_DIR)/libopengl.a: $(BLD_DIR)/opengl.o
	@echo "AR [libopengl.a]"
	@$(AR) $(ARFLAGS) $@ $(BLD_DIR)/opengl.o > /dev/null 2>&1

.PHONY: libopengl
libopengl: $(BLD_DIR)/libglad.a $(BLD_DIR)/libopengl.a ## Build libopengl.a

$(BLD_DIR)/test_opengl: test_opengl.c $(BLD_DIR)/libopengl.a $(BLD_DIR)/libglad.a
	@echo "TEST [test_opengl]"
	@$(CC) $(CFLAGS) test_opengl.c -o $@ -L$(BLD_DIR) -lopengl $(LDFLAGS)

.PHONY: test
test: libopengl $(BLD_DIR)/test_opengl ## Build and run test_opengl
	@cd $(BLD_DIR) && ./test_opengl

.PHONY: cppcheck
cppcheck: ## Run cppcheck
	@cppcheck opengl.c opengl.h

.PHONY: clean
clean: ## Clean build output
	@rm -rf $(BLD_DIR)
