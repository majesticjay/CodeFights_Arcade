def findEmailDomain(address):
    return (address[::-1].split('@'))[0][::-1]
