#!/usr/bin/python
import sys
import struct
def read_int(fd):
	buf=fd.read(4)
	while buf!='':
		entry = struct.unpack("I",buf)
		yield int(entry[0])
		buf=fd.read(4)
def pagetype(page):
	return page&3
def dump_pagetable(fd):
	addr=0
	for page in read_int(fd):
		if pagetype(page)==0:
			pass
		elif pagetype(page)==1:
			sys.stdout.write("%.3x:"%addr)
			flags=""
			if page&0x100: #P
				flags+="P"
			print "CoarsePT 0x%.6x%%%d|%s"%((page&~0x3ff),(page&0x1C0)>>5,flags)
		elif pagetype(page)==2:
			sys.stdout.write("%.3x:"%addr)
			flags=""
			if page&0x4:
				flags+="B" #?
			if page&0x8:
				flags+="C" #Cached
			if not page&0x10: #eXecute Never
				flags+="X"
			if page&0x100: #P
				flags+="P"
			if page&0x8000: #APX
				flags+="#"
			if page&0x10000: #shared
				flags+="S"
			if not page&0x20000: #non-Global
				flags+="G"
			if not page&0x40000: #Section (1MB)
				print "0x%.3x%%%d|%s?%.8x"%((page>>20),(page&0x1C0)>>5,flags,page)
			else: #Super Section (16MB)
				print "Supersection."
		else:
			sys.stdout.write("%.3x:"%addr)
			print "Type 11b RESERVED"
		addr+=1
def dump_lv2table(fd):
	addr=0
	for page in read_int(fd):
		if pagetype(page)==0:
			pass
		elif pagetype(page)==1:
			sys.stdout.write("%.2x:"%addr)
			print "Large Page"
		else:
			sys.stdout.write("%.2x:"%addr)
			flags=""
			if page&0x4:
				flags+="B" #?
			if page&0x8:
				flags+="C" #Cached
			if pagetype(page)==2: #eXecute Never
				flags+="X"
			if page&0x200: #APX
				flags+="#"
			if page&0x400: #Shared
				flags+="S"
			if not page&0x800: #non-Global
				flags+="G"
			print "0x%.5x|%s"%((page>>12),flags)
		addr+=1
fd=open(sys.argv[1])
dump_pagetable(fd)
#dump_lv2table(fd)
fd.close()

