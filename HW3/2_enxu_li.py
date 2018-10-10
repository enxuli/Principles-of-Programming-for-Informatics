def top_email_loop():
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
                mydict[tmplist[1]] = mydict.get(tmplist[1],0) + 1
        else:
            break
    fhand.close()
    max = 0
    for count in mydict.values():
        if count > max:
            max = count
    #in case there are multiple addresses with maximum number of msgs
    #we need anothger loop to print all these addresses
    for email,count in mydict.items():
        if count == max:
            print(email,str(count))

if __name__ == '__main__':
    top_email_loop()
