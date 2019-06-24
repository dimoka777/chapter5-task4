def funny_string(s):
    temp = list(map(ord, s))
    print(temp)
    j = -1
    for i in range(len(temp) - 1):
        print(str(temp[i + 1]) + ' ' + str(temp[i]) + ' ' + str(temp[j - 1]) + ' ' + str(temp[j]))
        if abs(temp[i + 1] - temp[i]) != abs(temp[j - 1] - temp[j]):
            print('Not Funny')
            break
        j -= 1
    print('Funny')



funny_string('acxz')