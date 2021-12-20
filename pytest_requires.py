# -*- coding: utf-8 -*-
# Copyright (C) Cardiff University (2021)

import pytest
from _pytest.outcomes import Skipped

__version__ = "0.1.0"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "requires(module[, module, ...], minversion=...): "
        "mark a test as requiring one or more optional dependencies; "
        "the test is skipped if any module cannot be imported or the "
        "minversion isn't met (the same minversion is used for all modules)",
    )


def evaluate_requires(item):
    """Evaluate requires marks on item, returning Skip if triggered.
    """
    for mark in item.iter_markers(name="requires"):
        try:
            modules = (mark.kwargs.pop("module"),)
        except KeyError:
            modules = mark.args

        for module in modules:
            pytest.importorskip(module, **mark.kwargs)


def pytest_collection_modifyitems(items):
    for item in items:
        if item.get_closest_marker("requires"):
            # evaluate the 'requires' marker
            try:
                evaluate_requires(item)
            except Skipped as exc:
                item.add_marker(
                    pytest.mark.skip(str(exc)),
                )
