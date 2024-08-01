# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service

class FabricServiceCallbacks(Service):
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info(f"Creating fabric: {service.name}")
        # Implement fabric configuration logic here

class NfaasFabric(ncs.application.Application):
    def setup(self):
        self.log.info('NFaaS Fabric Service RUNNING')
        self.register_service('fabric-servicepoint', FabricServiceCallbacks)

    def teardown(self):
        self.log.info('NFaaS Fabric Service FINISHED')