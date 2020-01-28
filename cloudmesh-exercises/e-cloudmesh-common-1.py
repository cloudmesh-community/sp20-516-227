
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

class ecc1:
# banner
    def banner(self):
        banner('Cloud Computing Week3')
# Heading
    def heading(self):
        HEADING()
        print('Cloud Computing Week3 heading')
# VERBOSE
    def verbose(self,m):
        VERBOSE(m)

if __name__=="__main__":
    e1 = ecc1()
    e1.banner()
    e1.heading()
    e1.verbose({'name': 'Xin'})
