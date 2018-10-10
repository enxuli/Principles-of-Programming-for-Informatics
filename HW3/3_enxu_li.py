def hour_freq():
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
                tmp = text_line.split()[5]
                hour = tmp.split(':')[0]
                mydict[hour] = mydict.get(hour, 0) + 1
        else:
            break
    print(mydict)
    mylist = [(hour,count) for hour,count in mydict.items()]

    mylist.sort()
    #here we have to assume that there is only one maximum
    #or will only display only one email address with the maximum number of msgs
    print(mylist[0][1],mylist[0][0])

if __name__ == '__main__':
    hour_freq()
