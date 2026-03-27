# Generate Diff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/K-Mickey/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/K-Mickey/python-project-50/actions)
[![Python CI](https://github.com/K-Mickey/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/K-Mickey/python-project-50/actions/workflows/pyci.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=K-Mickey_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=K-Mickey_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=K-Mickey_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=K-Mickey_python-project-50)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=K-Mickey_python-project-50)](https://sonarcloud.io/summary/new_code?id=K-Mickey_python-project-50)

## Description

**Gendiff** is a CLI utility that finds differences between two JSON or YAML files. 
It supports nested structures and outputs the result in one of three formats: stylish, plain, and JSON.

The project was created as part of the [Hexlet](https://hexlet.io) course.

### Key features
- Recursive comparison of nested data (dictionaries, lists, etc.).
- Internal representation decouples diff calculation from output formatting, making it easy to add new formatters.
- Extensible to support more file formats.

## Requirements

* UV 0.5 or higher
* Git

## Installation

[![asciicast](https://asciinema.org/a/91zGBMDnweQ8dAHh.svg)](https://asciinema.org/a/91zGBMDnweQ8dAHh)

Choose a place for the clone and run the following commands:

```bash
git clone https://github.com/K-Mickey/python-project-50.git
cd python-project-50
make install
make build
make package-install
```

After installation, you'll be able to launch the program from any directory on your computer.
Also, you can import the module `gendiff` and use the function `generate_diff` directly.

## Usage

### Supported file formats

[**JSON files**](https://asciinema.org/a/Vla4apoOryCTvLK3)

```bash
gendiff file1.json file2.json
```

[**YAML files**](https://asciinema.org/a/Vla4apoOryCTvLK3)

```bash
gendiff file1.yaml file2.yaml
or
gendiff file1.yml file2.yml
```

### Available formats

[**Stylish format**](https://asciinema.org/a/34FHItAmXaYpZcaV) - default, human‑readable tree with `+` and `-` markers

```bash
gendiff file1.json file2.json
# or
gendiff file1.yaml file2.yaml -f stylish
```

[**Plain format**](https://asciinema.org/a/34FHItAmXaYpZcaV) - text list of changes

```bash
gendiff file1.json file2.json -f plain
```

[**JSON format**](https://asciinema.org/a/34FHItAmXaYpZcaV) - structured machine‑readable format

```bash
gendiff file1.json file2.json -f json
```