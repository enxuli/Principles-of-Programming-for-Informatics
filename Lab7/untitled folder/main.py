import util,sys

def unittest():
    ret = util.get_Handle('testpath')
    expect = None
    assert(ret,expect)

def main():
    result = []
    for path in sys.argv:
        tmp = util.get_Handle(path)
        if tmp is None :
            print(None)
        else :
            result.append(tmp)
            print(tmp.read())
    return result

if __name__ == '__main__':
    main()
