from unidecode import *
def mapCommands(command, param = None):
    #motion
    if command == 'forward':
        return("<i style='color:blue;' class='fa fa-arrow-right' aria-hidden='true'></i>")
        #return('&#8594;')
    elif command == 'back':
        return("<i style='color:blue;' class='fa fa-arrow-left' aria-hidden='true'></i>")
        #return('&#8594;')
    elif command == 'up':
        return("<i style='color:blue;' class='fa fa-arrow-up' aria-hidden='true'></i>")
        #return('&#8593;')
    elif command == 'down':
        return("<i style='color:blue;' class='fa fa-arrow-down' aria-hidden='true'></i>")
        #return('&#8595;')
    elif command == 'right':
        return("<i style='color:blue;' class='fa fa-rotate-right' aria-hidden='true'></i>")
        #return('&#8631;')
    elif command == 'left':
        return("<i style='color:blue;' class='fa fa-rotate-left' aria-hidden='true'></i>")
        #return('&#8634;')
    elif command == 'hop':
        return("<i style='color:blue;' class='fa fa-arrows-v' aria-hidden='true'></i>")
    elif command == 'home':
        return("<i style='color:blue;' class='fa fa-times-circle-o' aria-hidden='true'></i>") 
    #trigger
    elif command == 'onflag':
        return("<i style='color:green;' class='fa fa-flag' aria-hidden='true'></i>")
    elif command == 'onclick':
        return("<i style='color:yellow;' class='fa fa-hand-o-up' aria-hidden='true'></i>")
    elif command == 'endstack':
        return("<font color=red>)</font>")
    elif command == 'onmessage':
        color = param if param else "black"
        return("<i style = color:" + color + " class='fa fa-envelope-open' aria-hidden='true'></i>")
    elif command == 'message':
        color = param if param else "black"
        return("<i style = color:" + color + " class='fa fa-envelope' aria-hidden='true'></i>")
    #sound
    elif command == 'playusersnd':
        return("<i style='color:green' class='fa fa-microphone' aria-hidden='true'></i>")
    elif command == 'playsnd':
        return("<i style='color:green' class='fa fa-volume-up' aria-hidden='true'></i>")
        #return('&#127908;')
    else:
        return(command)

def htmlHeaderFooter():
    return("""
        <html>
        <head>
        <link href="./fa/css/font-awesome.min.css" rel="stylesheet">
        <style>
        table tr td {border:1px solid black;}
        </style>
        <title>
        sjrcomp report
        </title>
        </head>
        <body>
        <table>
        ""","""
        </table>
        </html>""")

def strippedJson2htmlrow(strippedJson, maxpagenum = 2, maxspritenum = 2):
    returnString = "<tr>"
    returnString += ("<td>" + strippedJson["filename"] + "</td>")
    for pageNum in range(maxpagenum):
        if pageNum < len(strippedJson["pages"]):
            curPage = strippedJson["pages"][pageNum]
            for spriteNum in range(maxspritenum):
                if spriteNum < len(strippedJson[curPage]["sprites"]):
                    curSprite = strippedJson[curPage]["sprites"][spriteNum]
                    curSpriteInfo = strippedJson[curPage][curSprite]
                    returnString += "<td>"
                    returnString += curPage + ": " + curSpriteInfo["id"]
                    for (scriptIndex,aScript) in enumerate(curSpriteInfo["scripts"]):
                        returnString += "<br/>Script" + str(scriptIndex) + ":"
                        for (aCommand,aParam) in aScript:
                            if aParam == 'null' or aParam == 1:
                                returnString += (mapCommands(aCommand))
                            elif aCommand == 'message' or aCommand == 'onmessage':
                                returnString += mapCommands(aCommand,aParam)
                            else:
                                returnString += (mapCommands(aCommand,aParam) + str(aParam))
                    returnString += "</td>"
                else:
                    returnString += "<td>&nbsp;</td>"

        else:
            for spriteNum in range(maxspritenum):
                returnString += "<td>&nbsp;</td>"
    returnString += "</tr>\n"
    returnString = unidecode(unicode(returnString))
    return(returnString)

