#!/bin/bash
set -ex

# Format and check Python files
ruff format */*py
ruff check */*py
