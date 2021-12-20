# -*- coding: utf-8 -*-

import pytest


def test_help_message(testdir):
    result = testdir.runpytest(
        '--markers',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '@pytest.mark.requires(*',
    ])


@pytest.mark.parametrize(("module", "kwargs", "outcomes"), (
    ("sys", {}, dict(passed=1, failed=0, skipped=0)),
    ("_doesnotexist", {}, dict(passed=0, failed=0, skipped=1)),
    ("sys", {"minversion": "9999"}, dict(passed=0, failed=0, skipped=1)),
))
def test_marker(testdir, module, kwargs, outcomes):
    """Test that the requires marker works properly
    """
    testdir.makepyfile("""
        import pytest

        @pytest.mark.requires('{module}', **{kwargs})
        def test_one():
            pass
    """.format(module=module, kwargs=kwargs))

    result = testdir.runpytest()
    result.assert_outcomes(**outcomes)
