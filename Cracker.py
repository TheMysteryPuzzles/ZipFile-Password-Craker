import zipfile
from optparse import OptionParser
import threading
from queue import Queue


if __name__ == '__main__':

    queue = Queue()
    def extractFile(zFile, password):
        try:
            zFile.extractall(pwd=password)
            print("Password Found" + password)
        except:
            pass

    def main():
        print("Test")
        parser = OptionParser("usage: %prog [options] <zipfile> <disctionary>")
        parser.add_option("-f", dest="zname", type="string", help="specify zip file")
        parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
        (options, args) = parser.parse_args()

        if (options.zname == None) | (options.dname == None):
            print(parser.usage)
            exit(0)
        else:
            zname = options.zname
            dname = options.dname
            #createQueue(dname)
            zFile = zipfile.ZipFile(zname)
            passFile = open(dname)
            for line in passFile.readlines():
                password = line.strip("\n")
                t = threading.Thread(target=extractFile, args=(zFile, password))
                t.start()

    main()
