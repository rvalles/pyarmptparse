#!/usr/bin/python
import sys
fd=open(sys.argv[1])
decoded=""
buf=fd.read()
#print buf
def split_by_n(seq, n):
	while seq:
		yield seq[:n]
		seq = seq[n:]
#decoded = str(list(split_by_n(buf,2)))
decoded=[chr(int(buf[i:i+2],16)) for i in range(0, len(buf), 2)]
fd.close()
out=sys.stdout
out.write(''.join(decoded))
out.close()

