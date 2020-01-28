import os
from cloudmesh.common.util import banner


class Provider:

    def __init__(self, name):
        self.name = name

    def list(self):
        banner("list")
        os.system("multipass find")

    def shell(self):
        print("shell")
        os.system(f"multipass shell {self.name}")

    def run(self, command):
        # please add self.name so the command gets started on the named vm
        print(f"run {self.name} {command}")
        # improve next line
        os.system(f"multipass exec -- {command}")


if __name__ == "__main__":
    p = Provider("ubuntu-lts")
    p.run("list")
    p.shell()