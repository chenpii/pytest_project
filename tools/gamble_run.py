import random


def fuli():
    # (1-33)*6+(1-6)*1
    red_round = (1, 33)
    blue_round = (1, 6)
    return generate(6, 1, red_round, blue_round)


def tiyu():
    # (1-35)*5+(1-12)*2
    red_round = (1, 35)
    blue_round = (1, 12)
    return generate(5, 2, red_round, blue_round)


def generate(rtimes, btimes, red_round, blue_round):
    front = []
    back = []
    for i in range(rtimes):
        num = random.randint(*red_round)
        while (num in front):
            num = random.randint(*red_round)
        front.append(num)
    for i in range(btimes):
        num = random.randint(*blue_round)
        while (num in back):
            num = random.randint(*blue_round)
        back.append(num)
    front.sort()
    back.sort()
    return (front + ["+"] + back)


def shack(func, times):
    for i in range(times):
        print(*func(), sep=' ')


print(" .....................阿弥陀佛.......................")
print("                       _oo0oo_                      ")
print("                      o8888888o                     ")
print('                      88" . "88                     ')
print("                      (| -_- |)                     ")
print("                      0\\  =  /0                    ")
print("                   ___/‘---’\\___                   ")
print("                  .' \\|       |/ '.                ")
print("                 / \\\\|||  :  |||// \\             ")
print("                / _||||| -卍-|||||_ \\              ")
print("               |   | \\\\\\  -  /// |   |           ")
print("               | \\_|  ''\\---/''  |_/ |            ")
print("               \\  .-\\__  '-'  ___/-. /            ")
print("             ___'. .'  /--.--\\  '. .'___           ")
print("         ."" ‘<  ‘.___\\_<|>_/___.’>’ "".           ")
print("       | | :  ‘- \\‘.;‘\\ _ /’;.’/ - ’ : | |        ")
print("         \\  \\ ‘_.   \\_ __\\ /__ _/   .-’ /  /    ")
print("    =====‘-.____‘.___ \\_____/___.-’___.-’=====     ")
print("                       ‘=---=’                      ")
print("                                                    ")
print("...................佛祖保佑 ,今日暴富.................")

shack(fuli, 5)
print(" .....................阿弥陀佛.......................")
shack(tiyu, 5)
