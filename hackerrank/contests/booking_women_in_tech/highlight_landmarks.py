
words = raw_input().split()
n = raw_input()
landmarks = set(raw_input().split())

for word in words:
    if word in landmarks:
        print "<b>{0}</b>".format(word),
    else:
        print word,
