import os


class Ping(object):

    def run(self):
        with os.popen("ping -c1 127.0.0.1", "r") as rslt:
            for lines in rslt:
                print(lines.strip())

