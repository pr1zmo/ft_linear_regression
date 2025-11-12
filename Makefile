.PHONY: all clean run

PYTHON := python3
SRC_DIR := src

all: run

run:
	$(PYTHON) $(SRC_DIR)/main.py

clean:
	find $(SRC_DIR) -type f -name "*.pyc" -delete
	find $(SRC_DIR) -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true