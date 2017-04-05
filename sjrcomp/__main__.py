from sjrcompReader import *
from sjrcompParser import *
from sjrcompHTML   import *
from os import listdir,path


def keyFromStr(string):
	if string[2]=='_':
		return(string[3:5])
	else:
		return(string[2:4])

def listOfFileNames(dataDir):
    files = [f for f in listdir(dataDir)]
    files = [f for f in files if path.splitext(f)[1] == '.sjr']
    return(sorted(files, key = keyFromStr))

def main():
    dataPath = "./data"
    strippedJsonList = []
    for sjrFile in listOfFileNames(dataPath):
        strippedJsonList.append(stripJson(file2json(path.join(dataPath,sjrFile))))
    with open('report.html','w') as reportFile:
        (header,footer) = htmlHeaderFooter()
        reportFile.write(header)
        for strippedJson in strippedJsonList:
            reportFile.write(strippedJson2htmlrow(strippedJson))       
        reportFile.write(footer)

        

    

if __name__ == '__main__':
    main()