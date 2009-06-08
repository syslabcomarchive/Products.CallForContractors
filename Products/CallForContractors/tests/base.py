from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

ztc.installProduct('CallForContractors')
ztc.installProduct('CMFLinkChecker')
ztc.installProduct('ZCatalog')

ptc.setupPloneSite(products=['CallForContractors', 'CMFLinkChecker'])

class CallForContractorsTestCase(ptc.PloneTestCase):
    pass
    
class CallForContractorsFunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use
    doctest syntax. Again, we can put basic common utility or setup
    code in here.
    """
    
    class Session(dict):
        def set(self, key, value):
            self[key] = value

    def _setup(self):
        ptc.FunctionalTestCase._setup(self)
        self.app.REQUEST['SESSION'] = self.Session()


    def afterSetUp(self):
        roles = ('Member', 'Contributor')
        self.portal.portal_membership.addMember('contributor',
                                                'secret',
                                                roles, [])