def expanding(l: list) -> bool:
        d = [];
        for i in range(0, len(l)-1):
                d.append(abs(l[i+1]-l[i]));
        for i in range(0, len(d)-1):
                if (d[i] >= d[i+1]):
                        return False;
        return True;

def sumsquare(l: list) -> list:
        even = 0; odd = 0;
        for i in l:
                if (i % 2 == 0):
                        even += i*i;
                else:                                                   
                  odd += i*i;
        return [odd, even];                     
                                                
def transpose(m: list) -> list:
        r = len(m);
        c = len(m[0]);
        n = [];
        for i in range(0, c):
                row = [];
                for j in range(0, r):
                        row.append(m[j][i]);
                n.append(row);
        return n;
