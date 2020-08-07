#Palabra continue, apartir de continue, no se ejecuta
def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)


if __name__  == '__main__':
    run()