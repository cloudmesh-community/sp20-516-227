'''
E.Cloudmesh.Common.5

    Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

'''

from cloudmesh.common.StopWatch import StopWatch
from time import sleep


StopWatch.start('test')
sleep(10)

StopWatch.stop('test')

print("Total Time is:", StopWatch.get('test'))