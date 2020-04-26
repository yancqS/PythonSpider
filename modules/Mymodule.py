def say_hi():
    print('hi,this is my modules speaking')
    if __name__ == '__main__':
        print("run by itself")
    else:
        print("run by another module")


__version__ = '0.1'

say_hi()