# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ploneutfpr.atreferencepatch.testing import PLONEUTFPR_ATREFERENCEPATCH_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneutfpr.atreferencepatch is properly installed."""

    layer = PLONEUTFPR_ATREFERENCEPATCH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneutfpr.atreferencepatch is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneutfpr.atreferencepatch'))

    def test_browserlayer(self):
        """Test that IPloneutfprAtreferencepatchLayer is registered."""
        from ploneutfpr.atreferencepatch.interfaces import (
            IPloneutfprAtreferencepatchLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneutfprAtreferencepatchLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONEUTFPR_ATREFERENCEPATCH_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneutfpr.atreferencepatch'])

    def test_product_uninstalled(self):
        """Test if ploneutfpr.atreferencepatch is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneutfpr.atreferencepatch'))
