import os
from cloudmesh.common.util import banner


class Provider:

    def __init__(self, name):
        self.name = name

    def launch(self):
        banner(f"launch {self.name}")
        os.system(f"multipass launch --name {self.name}")
        print('\n')

    def start(self):
        banner(f"start {self.name}")
        os.system(f"multipass start {self.name}")
        print('\n'

    def list(self):
        banner("list")
        os.system("multipass find")

    def shell(self):
        print("shell")
        os.system(f"multipass shell {self.name}")

    def run(self, command):
        print(f"run {self.name} {command}")
        os.system(f"multipass exec -- {command}")

    def delete(self, purge=True):
        banner(f"delete {self.name}")
        os.system(f"multipass delete {self.name}")
        if purge:
            os.system(f"multipass purge")
        print('\n')


if __name__ == "__main__":
    p = Provider("ubuntu-lts")
    p.launch()
    p.start()
    p.list()
    p.shell()
    p.run("list")
    p.delete()