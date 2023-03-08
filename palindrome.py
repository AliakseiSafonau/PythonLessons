def palindrome_search(text):
    text = text.replace(' ', '')
    result = 'True'
    for i in range(0, len(text) // 2):
        if text[i] != text[-1 - i]:
            result = False
            break
    print(result)


palindrome_search('fghj hgf]')
