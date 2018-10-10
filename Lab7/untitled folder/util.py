def get_Handle(path):
    try:
        handle = open(path,'r')
    except:
        return None
    else:
        return handle

if __name__ == '__main__':
    print(get_Handle('testpath').read())
