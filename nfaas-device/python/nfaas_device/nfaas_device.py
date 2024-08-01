# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service

class DeviceServiceCallbacks(Service):
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info(f"Creating device: {service.name}")

        if service.name not in root.ncs__devices.device:
            vars = ncs.template.Variables()
            vars.add('name', service.name)
            vars.add('address', service.address)
            vars.add('authgroup', 'cisco')
            vars.add('ned-namespace', 'http://tail-f.com/ns/ned-id/' + service.ned_id.split(':')[0])
            vars.add('ned-id', service.ned_id)

            template = ncs.template.Template(service)
            template.apply('device-template', vars)
        else:
            self.log.info(f"Device {service.name} already exists in NSO")

class NfaasDevice(ncs.application.Application):
    def setup(self):
        self.log.info('NFaaS Device Service RUNNING')
        self.register_service('device-servicepoint', DeviceServiceCallbacks)

    def teardown(self):
        self.log.info('NFaaS Device Service FINISHED')