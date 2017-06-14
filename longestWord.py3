def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key=len)
