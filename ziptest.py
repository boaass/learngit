#coding=utf-8
#!/usr/bin/python

import sys
import os, os.path
import zipfile

def zip_ipa(filelist,zipfilename,basepath):
	#Check input ...
	fullzipfilename = os.path.abspath(zipfilename)
	print "fullzipfilename = " + fullzipfilename

	prefix_path = os.path.split(filelist[0])[0]

	# if os.path.exists(zipfilename):
		# os.remove(zipfilename)

	#Start to zip file ... 
	dest_file_list = []
	for temp_file in filelist:
		if os.path.isfile(temp_file):
			dest_file_list.append(temp_file)
		else:
			for root, dirlist, files in os.walk(temp_file):
				for filename in files:
					dest_file_list.append(os.path.join(root,filename))
	print "dest_file_list==================="
	print dest_file_list
	destZip = zipfile.ZipFile(fullzipfilename,"w")
	for eachfile in dest_file_list:
		destfile = eachfile[len(basepath):]
		destZip.write(eachfile,"1.txt")
		print "Zip file %s...to...%s" % (eachfile,destfile)
	destZip.close()
	print "Zip folder succeed!"
	print fullzipfilename


file_list = ["/Users/zhaichunlin/Desktop/5.txt","/Users/zhaichunlin/Desktop/2.txt","/Users/zhaichunlin/Desktop/3.txt","/Users/zhaichunlin/Desktop/4.txt"]

zip_ipa(file_list,"/Users/zhaichunlin/Desktop/1.ipa","/Users/zhaichunlin/Desktop/")

