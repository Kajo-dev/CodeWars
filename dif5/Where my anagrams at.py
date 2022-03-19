def anagrams(word, words):
    word_tab=[]
    words_tab=[]
    wynik=[]
    for i in range(len(word)):
        word_tab.append(word[i])
    word_tab.sort()
    for i in words:
        w=[]
        for k in range(len(i)):
            w.append(i[k])
            w.sort()
        words_tab.append(w)   
    for i  in range(len(words_tab)):
        if word_tab == words_tab[i]:
            wynik.append(words[i])
    return wynik

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))