'''
E.Cloudmesh.Common.2

    Develop a program that demonstrates the use of dotdict.
'''
from cloudmesh.common.dotdict import dotdict


class ecc2:
    def dot(self, data):
        data = dotdict(data)
        if data.name == 'Xin':
            print('The name is \'Xin\'')


if __name__ == "__main__":
    e2 = ecc2()
    e2.dot({'name': 'Xin'})
