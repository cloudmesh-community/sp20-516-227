# Xin Gu sp20-516-227

## E.Multipass.2

Primary instance could be created by simple multipass shell command (multipass start). When users try to start or shell into an instance by multipass before its existance, multipass will create the primary instance. There could only have one primary instance. When created, the primary instance will be built based on the latest Ubuntu LTS image and will be configured by default settings. 

Reference:
* <https://multipass.run/docs/primary-instance>