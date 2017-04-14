

word = raw_input().strip()

n = len(word)
vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

for i in xrange(n-1):
    if word[i] == word[i+1] or word[i] in vowels and word[i+1] in vowels:
        print "No"
        break
else:
    print "Yes"



