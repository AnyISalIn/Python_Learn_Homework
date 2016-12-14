def yhsj(layer):
    lst = []
    for i in range(0, layer):
        if i == 0:
            lst.append([1]); yield lst[0]
        else:
            lst.append([1])
            for number in range(1, i):
                lst[i].append(lst[i-1][number-1] + lst[i-1][number])
            lst[i].append(1)
            yield lst[i]

def main(layer):
    max_len = len(' '.join(str(x) for x in list(yhsj(layer))[-1]))
    for i in yhsj(layer):
        string = ' '.join([ str(x) for x in i ])
        yield(string.center(max_len))

if __name__ == '__main__':
    for i in main(10):
        print(i)
