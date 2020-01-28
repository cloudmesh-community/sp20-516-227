'''
E.Cloudmesh.Common.2

    Develop a program that demonstrates the use of dotdict.
'''
from cloudmesh.common.dotdict import dotdict

data = {
    'name': 'Xin'
}

data = dotdict(data)

if data.name == 'Xin':
    print('The name is \'Xin\'')