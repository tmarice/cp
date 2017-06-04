
from collections import defaultdict
import os


class Solution(object):

    def findDuplicate(self, paths):
        m = defaultdict(list)

        for path in paths:
            t = path.split(" ")
            base_path = t[0]
            file_names = t[1:]

            for f in file_names:
                op = f.find("(")
                cp = f.find(")")

                name = f[:op]
                content = f[op+1:cp]

                m[content].append(os.path.join(base_path, name))

        return [v for v in m.itervalues() if len(v) > 1]
