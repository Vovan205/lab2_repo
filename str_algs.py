def reverse(string):
    i = 0
    string2 = ''
    for ch in range(len(string)):
        cnt = len(string) - i - 1
        string2 = string2 + string[cnt]
        i = i + 1
    print(string2)
reverse("hello, world")