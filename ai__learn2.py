import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import operator



def classify(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0] ##返回数据的行数
	diffMat = np.tile(inX,(dataSetSize,1))-dataSet

	##print(inX)
	##生成册数样本与真实样本的差
	sqDiffMat = diffMat**2 #平方
	sqDistances = sqDiffMat.sum(axis = 1)  #所有行相加
	distances = sqDistances**0.5
	sortedDistIndices = distances.argsort()#返回从小到大的排序
	#print(sortedDistIndices)
	classCount = {}  #设立一个字典
	for i in range(k):
		##取出前k个样本数据
		voteIlabel = labels[sortedDistIndices[i]]
		#print(classCount)
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	print(sortedClassCount)
	return sortedClassCount[0]



def classifyperson(datingDataMat,datingLabels):
	first = float(input("airflight:"))
	second = float(input("play gaming:"))
	third = float(input("icecreame:"))
	inArr = np.array([first,second,third])
	print(inArr)
	norminArr = (inArr-minVals)/ranges
	finalresult = classify(norminArr,normMat,datingLabels,100)
	print(finalresult)



def file2martix(filename):  #将数据统一处理：读数据
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
			classlabelvector.append('didntLike')
		#print(classlabelvector)
		elif listfromline[-1] == 'smallDoses':
			classlabelvector.append('smallDoses')
		elif listfromline[-1] == 'largeDoses':
			classlabelvector.append('largeDoses')
		index += 1
	#print(returnMat)
	return returnMat,classlabelvector




def autoNorm(dataSet):  #将数据统一化，每个数据的差都是在0-1 的范围
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	#print(minVals)
	#总体数据范围
	ranges = maxVals - minVals
	#print(ranges)
	shape = np.shape(dataSet)
	#print(shape)
	#定义一个新的矩阵。用来存放归一化数据
	normDataSet = np.zeros(shape)
	#print(normDataSet)
	m = dataSet.shape[0]
	#print(m)
	normDataSet = dataSet - np.tile(minVals,(m,1)) ##每个数据与最小值的差
	#print(normDataSet)
	normDataSet = normDataSet / np.tile(ranges, (m, 1)) ##每个数据与最小值的差再除以总体数据范围
	#print(normDataSet)
	return normDataSet,ranges,minVals


if __name__ == '__main__':

    #打开的文件名
	filename = "data example.txt"
    #打开并处理数据
	file2martix(filename)
	datingDataMat,datingLabels = file2martix(filename)
	#print(datingDataMat)
	#print(datingLabels)
	#print(datingDataMat)
	#showdatas(datingDataMat, datingLabels)
	autoNorm(datingDataMat)
	normMat, ranges, minVals = autoNorm(datingDataMat)
	#datingClassTest()
	classifyperson(datingDataMat,datingLabels)