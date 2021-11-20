
if __name__ == '__main__':
    
    fp = open("new.txt", "r")
    
    line = fp.readline()
    while line != '':
        line = line.rstrip()
        print(line)
        line = fp.readline()
        
    fp.close()