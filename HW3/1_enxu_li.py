def count_day():
    print("Enter a file name:")
    while True:
        try:
            my_file = input()
            fhand = open(my_file,'r')
        except:
            print("Wrong name entered, enter again!")
        else:
            break;

    mydict = dict()

    while True:
        text_line = fhand.readline()
        if text_line:
            text_line = text_line.strip()
            if text_line.startswith('From'):
                tmplist = text_line.split()
                mydict[tmplist[2]] = mydict.get(tmplist[2],0) + 1
        else:
            break

    print(mydict)

if __name__ == '__main__':
    count_day()
