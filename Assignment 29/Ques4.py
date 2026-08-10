import sys
import os
import hashlib


def CalculateCheckSum(FileName):
    fobj1 = open(FileName,"rb")
    
    hobj = hashlib.md5()

    Buffer = fobj1.read(1000)

    while(len(Buffer)> 0 ):
        hobj.update(Buffer)
        Buffer = fobj1.read(1000)

    fobj1.close()

    return hobj.hexdigest()


def main():
    Ret1 = CalculateCheckSum(sys.argv[1])
    Ret2 = CalculateCheckSum(sys.argv[2])


    if(Ret1 == Ret2):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()