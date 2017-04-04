import zipfile
import json

def checkJson(jsondict):
  if "json" in jsondict:
    return True
  else:
    return False

def file2json(sfile):
  """
  Opens ScratchJr file unzips it and returns the json object
  """

  try:
    zfile = zipfile.ZipFile(sfile)
  except:
    print("Problem with %s" %sfile)
    return(None)

  try:
    zfile.extract("project/data.json")
  except:
    print("No data json in %s." %sfile)
    return(None)

  try:
    f = open('project/data.json')
    projectString = f.read().decode('utf-8')
  except:
    print("Problem reading project.json from %s. Permission problems?" %sfile)
    return(None)

  try:
    parsedJson = json.loads(projectString.replace('\t', '').replace('\n','').replace('\r',''))
    return(parsedJson)
  except:
    print("Not A JSON file in %s? " %sfile)
    return(None)

  if (checkJson(parsedJson)):
    return(parsedJson)
  else:
    print("Damaged json in file %s!" %sfile)
    return(None)
