#coding=utf-8
#!/usr/bin/python

import sys
import os,os.path

def checkParams():
	if len(sys.argv) < 3:
		print "参数无效"
		sys.exit()

	for i in xrange(1,len(sys.argv)):
		if "-p" == sys.argv[i]:
			dest_path = sys.argv[i+1]

	ReplaceSuffix(dest_path)

def ReplaceSuffix(documentPath):
	if not os.path.exists(documentPath):
		print "%s 目录不存在" %documentPath
		sys.exit()

	expand_path = os.path.expanduser(documentPath)
	print "绝对路径: " + expand_path

	files = os.listdir(expand_path)

	for filename in files:
		portion = os.path.splitext(filename)
		
		if portion[-1] == ".pic":
			newname = portion[0] + ".gif"

			print "filename = " + filename
			print "newname = " + newname
			os.rename(os.path.join(expand_path,filename), os.path.join(expand_path,newname))

checkParams()
