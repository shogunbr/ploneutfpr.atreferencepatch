# -*- coding: utf-8 -*-

from Products.Archetypes.exceptions import ReferenceException
from plone.uuid.interfaces import IUUID

def patched_deleteReference(self, referenceObject):
    try:
        sobj = referenceObject.getSourceObject()
        if sobj is None:
             return
        referenceObject.delHook(self, sobj,
                                referenceObject.getTargetObject())
    except ReferenceException:
        pass
    else:
        annotation = sobj._getReferenceAnnotations()
        try:
            annotation._delObject(IUUID(referenceObject, None))
        except (AttributeError, KeyError):
            pass
