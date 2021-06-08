from string import ascii_letters as alphabet

            


def main(): 
    shellcode = ""
    pchar = "41"
    pnum = 20
    p = pchar * pnum 




def str2Hex(s):
    return s.encode('utf-8').hex()

def str2MidEnd(s):

    # Check even string
    if len(s) % 2 != 0:
        return s

    rets = ""
    s = s.replace("0x", "")
    for i in range(len(s)): 
        if i % 2 == 0:
            chars = s[i:i+2]
            rets += chars[1] + chars[0]
    return rets









if __name__ == "__main__":
    main()
