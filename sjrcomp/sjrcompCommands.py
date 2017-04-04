catNames = [#Command Categories Names
  "yellow",
  "blue",
  "purple",
  "green",
  "orange",
  "red"]

catCommands = {} #all ScratchJr commands

catCommands["yellow"] = [
  "onflag",
  "onclick",
  "ontouch",
  "onmessage",
  "message"]

catCommands["blue"] = [
  "forward",
  "back",
  "up",
  "down",
  "left",
  "right",
  "hop",
  "home"]

catCommands["purple"] = [
  "say",
  "grow",
  "shrink",
  "same",
  "hide",
  "show"]

catCommands["green"] = [
  "playsnd",
  "playusersnd"]

catCommands["orange"] = [
  "wait",
  "stopmine",
  "setspeed",
  "repeat"]

catCommands["red"] = [
  "endstack",
  "forever",
  "gotopage"]

def catofCommand(command):
  """
  Returns the category name of the command
  if this is not a command it returns None
  """
  for cat in catNames:
    if (command in catCommands[cat]):
      return(cat)
  return(None)
