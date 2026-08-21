class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')
        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact = set(wordlist)
        cap = {}
        vow = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in cap:
                cap[lw] = w
            vw = devowel(w)
            if vw not in vow:
                vow[vw] = w

        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            elif q.lower() in cap:
                res.append(cap[q.lower()])
            elif devowel(q) in vow:
                res.append(vow[devowel(q)])
            else:
                res.append('')
        return res
