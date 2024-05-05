def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')

    version1 = list(map(int, version1))
    version2 = list(map(int, version2))
    
    while len(version1) and version1[-1] == 0:
        version1.pop()
    
    while len(version2) and version2[-1] == 0:
        version2.pop()
        
    print(version1)
    print(version2)
    if version1 == version2:
        return 0
    elif version1 > version2:
        return 1
    
    return -1



version1 = "0.1"
version2 = "1.1"

print(compareVersion(version1, version2))