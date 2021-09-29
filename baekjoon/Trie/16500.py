class Node(object) :
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        cursor = self.head
        for s in string :
            if s not in cursor.child:
                cursor.child[s] = Node(s)
            cursor = cursor.child[s]
        cursor.data = len(string)

    def search(self, idx, string):
        cursor = self.head
        for s in string :
            if cursor.data:
                return idx
            if s in cursor.child: cursor = cursor.child[s]
            else: return -1
            idx += 1
        if cursor.data:
            return idx
        return -1

target = input()
N = int(input())
myTrie = Trie()
for i in range(N):
    myTrie.insert(input())

cur = 0
while 0 <= cur < len(target):
    cur = myTrie.search(cur, target[cur:])
if cur == -1:
    print(0)
else:
    print(1)