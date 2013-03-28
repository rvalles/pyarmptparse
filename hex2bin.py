#!/usr/bin/python
import sys
fd=open(sys.argv[1])
decoded=""
buf=fd.read()
decoded=[chr(int(buf[i:i+2],16)) for i in range(0, len(buf), 2)]
fd.close()
out=sys.stdout
out.write(''.join(decoded))
out.close()
