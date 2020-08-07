#Validación del break
def run():
    for i in range(10000):
        print(i)
        if i == 5678:
            break


if __name__ == '__main__':
    run()