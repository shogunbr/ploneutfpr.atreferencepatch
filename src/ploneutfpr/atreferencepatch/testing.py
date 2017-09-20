# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneutfpr.atreferencepatch


class PloneutfprAtreferencepatchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=ploneutfpr.atreferencepatch)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneutfpr.atreferencepatch:default')


PLONEUTFPR_ATREFERENCEPATCH_FIXTURE = PloneutfprAtreferencepatchLayer()


PLONEUTFPR_ATREFERENCEPATCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEUTFPR_ATREFERENCEPATCH_FIXTURE,),
    name='PloneutfprAtreferencepatchLayer:IntegrationTesting'
)


PLONEUTFPR_ATREFERENCEPATCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEUTFPR_ATREFERENCEPATCH_FIXTURE,),
    name='PloneutfprAtreferencepatchLayer:FunctionalTesting'
)


PLONEUTFPR_ATREFERENCEPATCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONEUTFPR_ATREFERENCEPATCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneutfprAtreferencepatchLayer:AcceptanceTesting'
)
