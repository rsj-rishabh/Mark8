import os,sys
path = os.path.join(os.getcwd(),str(sys.argv[1]))
files = os.listdir(path)
for i,f in enumerate(files, 1):
	os.rename(os.path.join(path,f),os.path.join(path,'head{}.jpg'.format(i)))
	i=i+1 
