def quil2qasm(name):
        file = open(name, 'r')
        x = file.readlines()
        file2 = []
        for a in x:
                ref = list(a)
                out = ''
                for i in ref:
                        try:
                                x = int(i)
                                out = out+str(x)
                        except ValueError:
                                rand = 92
                if ref[0] == 'H':
                        file2.append('h q['+out+'];')
                allstring = ''
                for i in ref:
                        allstring = allstring+i
                lstring = allstring.split()
                if ref[0] == 'C':
                        file2.append('cx q['+lstring[1]+'],q['+lstring[2]+'];')
                if ref[0] == 'R':
                        strz1 = lstring[0]
                        strz2 = lstring[1]
                        splitstr = strz1.split('(')[1]
                        splitstr2 = splitstr.split(')')[0]
                        file2.append('u1('+str(splitstr2)+') q['+str(strz2)+'];')
        return file2
