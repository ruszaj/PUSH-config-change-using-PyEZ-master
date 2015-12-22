from jnpr.junos import Device
dev = Device('10.13.82.42')
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
rsp = cu.load( path="config-example.conf" )
cu.commit()

