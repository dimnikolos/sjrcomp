class command:
	def __init__(self,fa,jsonLex,reCode,smallDescription,largeDescription,category):
		self.fa = fa
		self.jsonLex = jsonLex
		self.reCode = reCode
		self.smallDescription = smallDescription
		self.largeDescription = largeDescription
		self.category = category

x = command("ga","greenFlat","Start on Green Flag","Starts the script when the Green Flag is tapped.","Triggering blocks")
listOfCommands = [

command("Start on Tap","Starts the script when you tap on the character.","Triggering blocks"),
command("Start on Bump","Starts the script when the character is touched by another character.","Triggering blocks"),
command("Start on Message","Starts the script whenever a message of the specified color is sent.","Triggering blocks"),
command("Send Message","Sends a message of the specified color.","Triggering blocks"),
command("Move Right","Moves the character a specified number of grid squares to the right.","Motion Blocks"),
command("Move Left","Moves the character a specified number of grid squares to the left.","Motion Blocks"),
command("Move Up","Moves the character a specified number of grid squares up.","Motion Blocks"),
command("Move Down","Moves the character a specified number of grid squares down.","Motion Blocks"),
command("Turn Right","Rotates the character clockwise a specified amount. Turn 12 for a full rotation.","Motion Blocks"),
command("Turn Left","Rotates the character counterclockwise a specified amount. Turn 12 for a full rotation.","Motion Blocks"),
command("Hop","Moves the character up a specified number of grid squares and then down again.","Motion Blocks"),
command("Go Home","Resets the character's location to its starting position. (To set a new starting position, drag the character to the location).","Motion Blocks"),
command("Say","Shows a specified message in a speech bubble above the character.","Looks Blocks"),
command("Grow","Increases the character's size.","Looks Blocks"),
command("Shrink","Decreases the character's size.","Looks Blocks"),
command("Reset Size","Returns the character to its default size.","Looks Blocks"),
command("Hide","Fades out the character until it is invisible.","Looks Blocks"),
command("Show","Fades in the character until it is fully visible.","Looks Blocks"),
command("Pop","Plays a \"Pop\" Sound","Sound Blocks"),
command("Play Recorded Sound","Plays a sound recorded by the user.","Sound Blocks"),
command("Wait","Pauses the script for a specified amount of time (in tenths of seconds).","Control Blocks"),
command("Stop","Stops all the characters' scripts.","Control Blocks"),
command("Set Speed","Changes the rate at which certain blocks are run.","Control Blocks"),
command("Repeat","Runs the blocks inside a specified number of times.","Control Blocks"),
command("End","Indicates the end of the script (but does not affect the script in any way).","End Blocks"),
command("Repeat Forever","Runs the script over and over.","End Blocks"),
command("Go to Page","Changes to the specified page of the project.","End Blocks")]