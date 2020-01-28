# banner
from cloudmesh.common.util import banner
banner('Cloud Computing Week3')

# Heading
from cloudmesh.common.util import HEADING
class headingexp():
    def doit(self):
        HEADING()
        print('Cloud Computing Week3')

heading = headingexp()
heading.doit()

# VERBOSE
from cloudmesh.common.debug import VERBOSE
m = {'name': 'Xin'}
VERBOSE(m)
