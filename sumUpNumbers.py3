def sumUpNumbers(inputString):
    l = re.findall(r"\d+",inputString)
    return sum([int(i) for i in l])
