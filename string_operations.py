from builtins import print

if __name__ == '__main__':
    s = 'abcdefghaa'
    print(len(s))
    print(s[1:4])
    print(s.count('a'))
    print(s.index('e'))
    print(s.rindex('a'))

    print(s[:4])
    print(s[4:])
    print(s[-2:])
    print(s[-5:-3])

    print('------------------')
    s2 = 'abc\ndef\t\tefg\\eyet\ye'
    print(s2)

    print(ord('a'))
    print(ord('A'))
    print(ord('\t'))
    print(ord('\n'))

    s3 = 'abc\b'
    print(s3)

    s4 = '   abcd   '
    s4 = s4.strip()
    s5 = 'abcd'
    if s4==s5:
        print('s4 and s5 equal')
    else:
        print('s4 and s5 not equal')
    s6 = '542352\t34535334\t513516521656\t6636'
    print(s6.split('\t'))

    s7 = 'can\'t'
    s7 = "can't" + "cite"
    print(s7)
