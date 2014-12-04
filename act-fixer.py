import re
import mmap
import sys
import os
	
	
sirgay=0
seek=12 #12 normal 10 skill lencea
size=4 #4 normal 5 skill lencea
count=0
seek_02byte=32
seek_02byte_write='\x01' #version 1 .act
lista_fisiere=[]
print "DragonNest .act fixer for newer official clients"
print "Created by Alin1337 - catalin@live.jp\n"
if len(sys.argv) != 2:
	print "usage: act-script.py folder \nex: act-script.py char/academic\nFolder must be in same directory as this executable!"
	sys.exit()

for file in os.listdir(sys.argv[1]):
	if file.endswith(".act"):
		print file
		lista_fisiere.append(file)
		count+=1

if count > 1:
	print "Found %d files , continue ? (this will overwrite the files)  (Y/n)"%(count)
	if(raw_input() == 'n'):
		print "Ok i will exit then."
		sys.exit()
	
for i in lista_fisiere: #aici vine actiunea aia mare ^^
	f=open(sys.argv[1]+'/'+i,'rb+')
	print "Fixing script",sys.argv[1]+'/'+i,'\n'
	buffer =f.read() #.replace(b'\x53\x74\x61\x6e\x64',b'\x74\x65\x73\x31')
	#1 NORMAL ACT 								1st 			   3rd p1				                                                     								    4x 00 -- diff
	unk1=re.compile(b"[\x30-\x7A][\x30-\x7A][\x30-\x7A]\x00[\x00-\xFF]\x00\x00\x00[\x00-\xFF]\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[\x01-\xFF]")
	#2
	#unk1=re.compile(b"[\x30-\x7A][\x30-\x7A][\x30-\x7A]\x00[\x00-\xFF]\x00\x00\x00[\x00-\xFF]\x00\x00\x00\x00\x00\x00\x00[\x01-\xFF]\x00\x00\x00[\x01-\xFF]\x00\x00\x00")
	#3
	#unk1=re.compile(b"[\x30-\x7A][\x30-\x7A][\x30-\x7A]\x00[\x00-\xFF]\x00\x00\x00[\x00-\xFF]\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[\x01-\xFF]\x00\x00\x00[\x01-\xFF]\x00\x00\x00")
	#4 skill lencea
	#unk1=re.compile(b"[\x30-\x7A][\x30-\x7A][\x30-\x7A]\x00[\x01-\xFF]\x00\x00\x00\x00[\x01-\xFF]\x00\x00\x00\x00[\x01-\xFF]\x00\x00\x00[\x01-\xFF]\x00\x00\x00[\x01-\xFF]")

	lista= [m.start() for m in re.finditer(unk1,buffer)]
	


	VDATA = mmap.mmap(f.fileno(),0)	#Load fisier in mmemory

	#add 01 ^^
	VDATA.seek(seek_02byte)
	VDATA.write_byte(seek_02byte_write)
	print "Wrote 0x01 byte at offset 32(dec)"
	def deleteFromMmap(start,end):
		global VDATA
		length = end - start
		size = len(VDATA)
		newsize = size - length

		VDATA.move(start,end,size-end)
		VDATA.flush()
		VDATA.close()
		f.truncate(newsize)
		VDATA = mmap.mmap(f.fileno(),0)
		print "->deleted from ",start,end
		
		
	for i in lista:
		deleteFromMmap(i+seek-sirgay,i+seek+size-sirgay) #cea mai smechera formula din 2000 pana acum!
		sirgay+=size
	sirgay = 0
	print "-- [DONE] --\n\n"
	f.close()

