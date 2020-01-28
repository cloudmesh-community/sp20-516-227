'''
E.Cloudmesh.Common.4

    Develop a program that demonstrates the use of cloudmesh.common.Shell.

'''

from cloudmesh.common.Shell import Shell


class ec4:
    def list(self):
        result1 = Shell.execute('ls', ['-l', '-a'])
        print(result1)

    def pwd(self):
        result2 = Shell.pwd()
        print(result2)


if __name__ == '__main__':
    e4 = ec4()
    e4.list()
    e4.pwd()
