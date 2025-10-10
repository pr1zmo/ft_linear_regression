.PHONY: all clean run

PYTHON := python3
SRC_DIR := src

all: run

run:
	@for file in $(SRC_DIR)/*.py; do \
		echo "Running $$file..."; \
		$(PYTHON) $$file; \
	done

clean:
	find $(SRC_DIR) -type f -name "*.pyc" -delete
	find $(SRC_DIR) -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true