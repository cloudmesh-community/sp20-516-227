'''
E.Cloudmesh.Common.4

    Develop a program that demonstrates the use of cloudmesh.common.Shell.

'''

from cloudmesh.common.Shell import Shell

result1 = Shell.execute('ls',['-l', '-a'])
print(result1)

result2 = Shell.pwd()
print(result2)
