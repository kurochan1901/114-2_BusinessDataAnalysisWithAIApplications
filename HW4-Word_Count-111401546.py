# 企管四 111401546 
lyric = ["I'm trying to hold my breath",
          "Let it stay this way",
          "Can't let this moment end",
          "You set off a dream with me",
          "Getting louder now",
          "Can you hear it echoing?",
          "Take my hand",
          "Will you share this with me?",
          "'Cause darling without you",
          "All the shine of a thousand spotlights",
          "All the stars we steal from the nightsky",
          "Will never be enough",
          "Never be enough",
          "Towers of gold are still too little",
          "These hands could hold the world but it'll",
          "Never be enough", "For me",
          "Never, never", "Never, for me",
          "Never enough", "For me"]

def neverEnough2():
    """ Word counts of Lyric of "NEVER ENOUGH"
        from the movie, The Greatest Showman """
    
##  -------------------------------------------
##  >>>>>  Word Count ..........
##  -------------------------------------------
    for i in [-6, -4, -2, -1]:  # NOTE: There's no switch-case in Python.
        if i == -1:
            lyric.insert(i, lyric[i])
        if i == -2 or i == -1:
            lyric.insert(i, lyric[i])
        lyric.insert(i, lyric[i])

    print(" --- << Never Enough 2 >> --- ")    
    for verse in lyric:         
        print(verse, end='\n')
    
    ##  Tokenizing words (comprehension)
    lyric_to_words = [w.rstrip('?,') for verse in lyric for w in verse.split(" ")]   
    
    ##  Word counting (comprehension)
    word_count_dic = {word: sum(1 for wordCount in lyric_to_words if word == wordCount) for word in set(lyric_to_words)}

    ##  Sorting (comprehension)
    word_sorted = sorted(word_count_dic.keys())         #產生一個按字母排序好的單字清單

    value_sorted = [word_count_dic[k] for k in sorted(word_count_dic.keys())]

    ##  Output the Word-Count results (comprehension)
    print("\n\n --- <<  Word-Counting the lyric of Never Enough >> --- ")
    print("\n".join(f"{w}{' '*(20 - len(w)-(1 if v >= 10 else 0))}{v}" for w,v in zip(word_sorted, value_sorted)))


neverEnough2()
'''
    ##  Tokenizing words...
    lyric_to_words = []
    for verse in lyric:
        words = verse.split(" ")
        for w in words:
            w = w.rstrip('?')                       #移除字串右邊的指定字元(?,)
            lyric_to_words.append(w.rstrip(','))


    ##  Word counting...
    lyric_to_wordset = set(lyric_to_words)
    
    word_count_dic = {}
    for word in lyric_to_wordset:
        value = 0
        for wordCount in lyric_to_words:
            if word == wordCount:
                value = value + 1
        word_count_dic[word] = value

    ##  Sorting......
    word_sorted = sorted(word_count_dic.keys())
    values = list(word_count_dic.values())

    value_sorted = []
    for k in word_sorted:
        i = 0
        for k1 in word_count_dic.keys():
            if k == k1 :
                value_sorted.append(values[i])
            i = i + 1

                        
    ##  Output the Word-Count results... 
    print("\n\n --- <<  Word-Counting the lyric of Never Enough >> --- ")

    for i in range(len(value_sorted)):
        nb = 20 - len(word_sorted[i])
        if value_sorted[i] >= 10:
           nb = nb - 1
        print(word_sorted[i], ' '*nb, value_sorted[i])
    
'''
