from collections import deque, defaultdict
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.count = 0
        self.child = {}
class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cursor = self.head
        for s in string:
            if s not in cursor.child:
                cursor.child[s] = Node(s)
            cursor.child[s].count += 1
            cursor = cursor.child[s]
        cursor.data = string

    def search(self, string):
        cursor = self.head
        for s in string:
            if s in cursor.child:
                cursor = cursor.child[s]
            else:
                return False

        if cursor.data == string:
            return True
        else:
            return False

    def starts_with(self, prefix, num):
        cursor = self.head
        ret = []
        for s in prefix:
            if s in cursor.child:
                cursor = cursor.child[s]
            else:
                return 0
        return cursor.count

def solution(words, queries):
    answer = []
    myTrie = Trie()
    reversedTrie = Trie()
    wl = defaultdict(int)
    for word in words:
        wordLen = len(word)
        wl[wordLen] += 1
        myTrie.insert(word)
        reversedTrie.insert(word[::-1])

    for query in queries:
        queryLen = len(query)
        cnt=0
        if query.startswith('?'):
            query = query[::-1]
            for i in range(len(query)):
                if query[i] == '?':
                    break
                cnt+=1
            if cnt == 0 :
                answer.append(wl[queryLen])
            else:
                answer.append(reversedTrie.starts_with(query[:cnt], queryLen))
        else:
            for i in range(len(query)):
                if query[i] == '?':
                    break
                cnt += 1
            answer.append(myTrie.starts_with(query[:cnt], queryLen))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))