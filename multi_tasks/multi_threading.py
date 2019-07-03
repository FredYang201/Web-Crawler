import threading

def sing():
    for i in range(5):
        print('------singing----------')


def dance():
    for j in range(5):
        print('------dancing---------')


def main():
    t1 = threading.Thread(target = sing)
    t2 = threading.Thread(target = dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()



