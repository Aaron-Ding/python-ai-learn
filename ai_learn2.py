import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt


def file2martix(filename):
	fr = open(filename)
	#print(fr)
	arrayOfLines = fr.readlines()
	#print(arrayOfLines)

	numberOfLines = len(arrayOfLines)
	#print(numberOfLines)

	returnMat = np.zeros((numberOfLines,3)) #生成一个秩为3的子集
	#print(returnMat)

	classlabelvector = []
	index = 0
	
	
	for line in arrayOfLines:
		
		line = line.strip() ##规整数据格式
		#print(line)
		listfromline = line.split('\t')  ##把数据变成一个一个的子集
		#print(listfromline[0:3])
		returnMat[index,:] = listfromline[0:3]  ##把之前秩为三的子集每一个元素附上一个值
		#print(returnMat[index,:])
		##print(listfromline[-1])
		if listfromline[-1] == 'didntLike':
			classlabelvector.append(1)
		#print(classlabelvector)
		elif listfromline[-1] == 'smallDoses':
			classlabelvector.append(2)
		elif listfromline[-1] == 'largeDoses':
			classlabelvector.append(3)
		index += 1
	#print(classlabelvector)
	return returnMat,classlabelvector

def showdatas(datingDataMat,datingLabels):
	font = FontProperties(fname=r"c:\\windows\\fonts\\simsun.ttc", size=14)
	fig,axs = plt.subplots(nrows =2,ncols =2,sharex = False,sharey = False,figsize=(13,8))
	numberOfLabels = len(datingLabels)
	print(numberOfLabels)




if __name__ == '__main__':
    #打开的文件名
	filename = "111.txt"
    #打开并处理数据
	file2martix(filename)
	datingDataMat,datingLabels = file2martix(filename)
	print(datingDataMat)
	print(datingLabels)
	showdatas(datingDataMat, datingLabels)