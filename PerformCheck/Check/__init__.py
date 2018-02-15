import dis

def chained_compare():
        a = 1.2
        b = 1.3
        c = 1.1
        a < b < c

def and_compare():
        x = 1.2
        y = 1.3
        z = 1.1
        x < y and y < z

dis.dis(chained_compare)
dis.dis(and_compare)