from sjrcompReader import *
from sjrcompParser import *
from sjrcompHTML   import *
from os import listdir,path

def listOfFileNames(dataDir):
    files = [f for f in listdir(dataDir)]
    files = [f for f in files if path.splitext(f)[1] == '.sjr']
    return(files)
    
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