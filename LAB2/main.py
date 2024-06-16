import ping3
import sys

def GetMTU(host):
    try:
        result = ping3.ping(host)
    except:
        print('Неизвестная ошибка внутри ping3')
        return 1
    if not result:
        print('Недоступный хост или icmp заблокирован')
        return 1

    L = 0
    R = 65508
    while R - L > 1:
        M = (L + R) // 2
        try:
            result = ping3.ping(host, size=M, timeout=1)
        except:
            print('Неизвестная ошибка внутри ping3')
            return 1
        if result:
            L = M
        else:
            R = M
    if L == False:
        print('Хост недоступен')
        return 1
    print('MTU =', L, '(' + str(L + 28) + ')')
    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Использование: python3 main.py <host>')
        exit(0)
    GetMTU(sys.argv[1])
