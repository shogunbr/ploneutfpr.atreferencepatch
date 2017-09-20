# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable as \
    INonInstallableProfiles
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as \
    INonInstallableProducts
from zope.interface import implementer


@implementer(INonInstallableProducts)
class HiddenProducts(object):

    def getNonInstallableProducts(self):
        """Returns a list of products that should not be available for
           installation.
        """
        return [
            'ploneutfpr.atreferencepatch',
        ]


@implementer(INonInstallableProfiles)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Returns a list of profiles that should not be available for
           installation at portal creation time.

           The usual use-case is to prevent extension profiles from showing up,
           that will be installed as part of the site creation anyways.
        """
        return [
            'ploneutfpr.atreferencepatch:default',
        ]

