
def getSprites(json):
    return([json["json"][aPage]["sprites"] for aPage in json["json"]["pages"]])

def stripScript(script):
    newScript = []
    if type(script) is list:
        if type(script[0]) is not list:
            if len(script) > 1:
                newScript = (script[0],script[1])
            else:
                newScript = script[0]
        else:
            for sc in script:
                newScript.append(stripScript(sc))
    return(newScript)


def stripJson(oldJson,filename = None):
    newJson = {}
    if filename:
    	newJson["filename"] = filename
    else:
    	newJson["filename"] = oldJson["name"]
    oldJson = oldJson["json"]
    newJson["pageNum"]=len(oldJson["pages"])
    newJson["pages"] = oldJson["pages"]
    for page in oldJson["pages"]:
        newJson[page] = {}
        newJson[page]["spriteNum"] = len(oldJson[page]["sprites"])
        newJson[page]["sprites"] = []
        for aSprite in oldJson[page]["sprites"]:
            newJson[page]["sprites"].append(aSprite)
            newJson[page][aSprite] = {}
            newJson[page][aSprite]["id"] = oldJson[page][aSprite]["id"]
            newJson[page][aSprite]["scripts"] = []
            if "scripts" in oldJson[page][aSprite]:
            	for aScript in oldJson[page][aSprite]["scripts"]:
                	newJson[page][aSprite]["scripts"].append(stripScript(aScript))
    return(newJson)
    