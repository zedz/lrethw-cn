import re
import sys

infile = open(sys.argv[1]).readlines()

while True:
    mline = False
    try:
        exp = raw_input("> ")

        if exp == "!":
            mline = True
            exp = []
            l = raw_input()
            while l:
                exp.append(l)
                l = raw_input()

            r = re.compile("\n".join(exp), re.X)
        else:
            r = re.compile(exp)

        for i, line in enumerate(infile):
            if r.match(line):
                print "%.4d: %s" % (i, line),
    except EOFError:
        print "\nBYE"
        sys.exit(0)
    except Exception, e:
        print "ERROR", e

