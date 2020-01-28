'''
E.Cloudmesh.Common.3

    Develop a program that demonstrates the use of FlatDict.

'''
from cloudmesh.common.Flatdict import FlatDict

data = {
    'name': 'Xin',
    'address': {
        'city': 'Indy',
        'state': 'IN'

    }
}

flat = FlatDict(data, sep=',')

print(flat)