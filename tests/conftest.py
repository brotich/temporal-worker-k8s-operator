# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Fixtures for jenkins-k8s charm tests."""

import pytest


def pytest_addoption(parser: pytest.Parser):
    """Parse additional pytest options.

    Args:
        parser: pytest command line parser.
    """
    # The prebuilt charm file.
    parser.addoption("--charm-file", action="append", default=[])
    # The image name:tag.
    parser.addoption("--temporal-worker-image", action="store", default="")
