while True:
    try:
        letters = input()
        lamps = int(input())
        rawMessage = input().split()
        for i in range(len(rawMessage)):
            rawMessage[i] = int(rawMessage[i])

        message = []

        for i in range(lamps):
            message.append(letters[rawMessage[i] - 1])

        print(''.join(message))

    except EOFError:
        break
