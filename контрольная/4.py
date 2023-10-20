def is_similar(word1, word2):
    if len(word1) != len(word2):
        return False
    
    differences = 0
    for str1, str2 in zip(word1, word2):
        if str1 != str2:
            differences += 1
        if differences > 1:
            return False

    return differences == 1


def test_is_similar():
    result1 = is_similar('пень', 'лень')
    if result1 == True:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    result2 = is_similar('вторник', 'вторнек')
    if result2 == True:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    result3 = is_similar('город', 'огород')
    if result3 == True:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    result4 = is_similar('перец', 'конец')
    if result4 == False:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    result5 = is_similar('вор', 'ворон')
    if result5 == False:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    result6 = is_similar('перец', 'конец')
    if result6 == False:
        print("Test 6 passed")
    else:
        print("Test 6 failed")

test_is_similar()
