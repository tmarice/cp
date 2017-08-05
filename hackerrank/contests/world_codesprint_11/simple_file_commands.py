
from collections import defaultdict
import heapq


class FileStorage(object):

    def __init__(self):
        self._storage = defaultdict(dict)
        self._free_sufices = defaultdict(list)
        self._max_suffix = defaultdict(int)


    def _find_suffix(self, file_name):
        try:
            suffix = heapq.heappop(self._free_sufices[file_name])
        except:
            suffix = 0

        if len(self._free_sufices[file_name]) == 0:
            heapq.heappush(self._free_sufices[file_name], suffix+1)

        return suffix


    def _del_suffix(self, name, suffix):
        heapq.heappush(self._free_sufices[name], suffix)


    def crt(self, file_name):
        suffix = self._find_suffix(file_name)

        if suffix > 0:
            return "{0}({1})".format(file_name, suffix)
        else:
            return file_name


    def del_file(self, file_name):
        sp = file_name.split("(")
        if len(sp) == 2:
            name, suffix = sp
            suffix = int(suffix.split(")")[0])
        else:
            name = sp[0]
            suffix = 0

        self._del_suffix(name, suffix)

        return file_name


    def rnm(self, file_name1, file_name2):
        self.del_file(file_name1)
        new_file = self.crt(file_name2)

        return "r {0} -> {1}".format(file_name1, new_file)


def main():
    q = int(raw_input())


    fs = FileStorage()
    for _ in range(q):
        cmds = raw_input().split()

        if cmds[0] == "crt":
            print "+ " + fs.crt(cmds[1])
        elif cmds[0] == "del":
            print "- " + fs.del_file(cmds[1])
        else:
            print fs.rnm(cmds[1], cmds[2])


main()
