# pytest-requires

[![PyPI version](https://img.shields.io/pypi/v/pytest-requires.svg)](https://pypi.org/project/pytest-requires)

[![Python versions](https://img.shields.io/pypi/pyversions/pytest-requires.svg)](https://pypi.org/project/pytest-requires)

[![Build status](https://github.com/duncanmmacleod/pytest-requires/actions/workflows/build.yml/badge.svg)](https://github.com/duncanmmacleod/pytest-requires/actions/workflows/build.yml)

A pytest plugin to elegantly skip tests with optional requirements

------------------------------------------------------------------------

This [pytest](https://github.com/pytest-dev/pytest) plugin was generated
with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with
[\@hackebrot](https://github.com/hackebrot)\'s
[cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin)
template.

## Features

- decorate tests that require optional modules (with an optional minimum version)
  and gracefully skip them when the requirements aren't importable

## Requirements

- pytest

## Installation

You can install \"pytest-requires\" via
[pip](https://pypi.org/project/pip/) from
[PyPI](https://pypi.org/project):

```shell
pip install pytest-requires
```

## Usage

### How to use pytest-requires

With pytest-requires, tests can be marked as requiring an external module
as follows:

```python
@pytest.mark.requires("dateutil")
def test_date_parsing():
    assert date_parsing() == RESULT
```

In this example if the python-dateutil module isn't installed the test is
skipped.
The import testing is all performed by pytest's builtin
[`importorskip`](https://docs.pytest.org/en/latest/how-to/skipping.html#skipping-on-a-missing-import-dependency)
function.

Notes:

- the `minversion` keyword can be given to specifiy a minimum acceptable
  version for the required module
- multiple modules can be given as positional arguments, with the decorated
  tested being skipped if any of the given modules cannot be imported
- in the case of multiple modules, only a single `minversion` can be given,
  and will be used for all modules; if an independent `minversion` is required
  for each module, use multiple `@pytest.mark.requires` decorators.

### Why not just use `pytest.importorskip`?

`pytest.importorskip` is designed to import a module and add the module
to the namespace (of the module, or the test function).
If the optional module isn't used in the test itself, but is really a
requirement of the function _being tested_, the call to `importorskip`
less elegant (in the author's opinion) than a decorator call.

## Contributing

Contributions are very welcome, please open a Pull Request.

## License

Distributed under the terms of the
[MIT](http://opensource.org/licenses/MIT) license, \"pytest-requires\"
is free and open source software

## Issues

If you encounter any problems, please
[file an issue](https://github.com/duncanmmacleod/pytest-requires/issues)
along with a detailed description.
