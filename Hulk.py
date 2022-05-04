def main():
    n = int(input())
    hate, love, that, it = 'I hate ', 'I love ', 'that ', 'it'
    text = ''
    i = 1
    if n == 1:
        print('I hate it')
    else:
        while i <= n:
            if i%2 == 0:
                text += love
            else:
                text += hate
            if i+1 <= n:
                text += that
            i += 1
 
        text += it
        print(text)
 
main()
