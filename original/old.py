import random

def findscore(x, y, z):
	global mon1list, mon2list, mon3list
	ScoreList = []
	if (OnePokemon == True or RandomChoice == True):
		mon2Find = ProgramMatchupList.index(y)
		mon3Find = ProgramMatchupList.index(z)
		for countingvar in range (SheetLength):
			mon2list.append(ProgramMatchupList[mon2Find + countingvar + 1])
			mon3list.append(ProgramMatchupList[mon3Find + countingvar + 1])
		for countingvar2 in range (len(mon1list)):
			appendnote = 'l'
			if (mon1list[countingvar2] == 'w' or mon1list[countingvar2] == 'm'):
				appendnote = mon1list[countingvar2]
			if (appendnote != 'w' and (mon2list[countingvar2] == 'w' or mon2list[countingvar2] == 'm')):
				appendnote = mon2list[countingvar2]
			if (appendnote != 'w' and (mon3list[countingvar2] == 'w' or mon3list[countingvar2] == 'm')):
				appendnote = mon3list[countingvar2]
			ScoreList.append(appendnote)
		if (MonsBeaten == True):
			ListScore = 1
			for countingvar3 in range (len(MonsList)):
				MonUsed = MonsList[countingvar3]
				MonIndex = ProgramIDList.index(MonUsed)
				if (ScoreList[MonIndex] != 'w'):
					ListScore = 0		
			if (ListScore != 0):
				ListScore = 0
				for countingvar4 in range (len(ScoreList)):
					if (ScoreList[countingvar4] == 'w'):
						ListScore = ListScore + 1
					elif (ScoreList[countingvar4] == 'm'):
						ListScore = ListScore + .5
					elif (ScoreList[countingvar4] == 'l'):
						ListScore = ListScore + 0
		else:
			ListScore = 0
			for countingvar5 in range (len(ScoreList)):
				if (ScoreList[countingvar5] == 'w'):
					ListScore = ListScore + 1
				elif (ScoreList[countingvar5] == 'm'):
					ListScore = ListScore + .5
				elif (ScoreList[countingvar5] == 'l'):
					ListScore = ListScore + 0
	elif (TwoPokemon == True):
		mon3Find = ProgramMatchupList.index(z)
		mon3list = []
		for countingvar in range (SheetLength):
			mon3list.append(ProgramMatchupList[mon3Find + countingvar + 1])
		for countingvar2 in range (len(mon1list)):
			appendnote = 'l'
			if (mon1list[countingvar2] == 'w' or mon1list[countingvar2] == 'm'):
				appendnote = mon1list[countingvar2]
			if (appendnote != 'w' and (mon2list[countingvar2] == 'w' or mon2list[countingvar2] == 'm')):
				appendnote = mon2list[countingvar2]
			if (appendnote != 'w' and (mon3list[countingvar2] == 'w' or mon3list[countingvar2] == 'm')):
				appendnote = mon3list[countingvar2]
			ScoreList.append(appendnote)
		if (MonsBeaten == True):
			ListScore = 1
			for countingvar3 in range (len(MonsList)):
				MonUsed = MonsList[countingvar3]
				MonIndex = ProgramIDList.index(MonUsed)
				if (ScoreList[MonIndex] != 'w'):
					ListScore = 0		
			if (ListScore != 0):
				ListScore = 0
				for countingvar4 in range (len(ScoreList)):
					if (ScoreList[countingvar4] == 'w'):
						ListScore = ListScore + 1
					elif (ScoreList[countingvar4] == 'm'):
						ListScore = ListScore + .5
					elif (ScoreList[countingvar4] == 'l'):
						ListScore = ListScore + 0
		else:
			ListScore = 0
			for countingvar5 in range (len(ScoreList)):
				if (ScoreList[countingvar5] == 'w'):
					ListScore = ListScore + 1
				elif (ScoreList[countingvar5] == 'm'):
					ListScore = ListScore + .5
				elif (ScoreList[countingvar5] == 'l'):
					ListScore = ListScore + 0
	#elif (ThreePokemon == True):
		#mon3list = []
	return ListScore

def rearrangemaxvalue():
	global MonComboList
	global MonComboScoreList
	global MonComboIDList

	xreplacelist = []
	yreplacelist = []
	zreplacelist = []

	for z in range(50):
		ilist = max(MonComboScoreList)
		index = MonComboScoreList.index(ilist)
		xreplace = MonComboList[index]
		yreplace = MonComboScoreList[index]
		zreplace = MonComboIDList[index]
		xreplacelist.append(xreplace)
		yreplacelist.append(yreplace)
		zreplacelist.append(zreplace)
		MonComboList.remove(xreplace)
		MonComboScoreList.remove(yreplace)
		MonComboIDList.remove(zreplace)
	
	MonComboList = xreplacelist
	MonComboScoreList = yreplacelist
	MonComboIDList = zreplacelist

	return MonComboList
	return MonComboIDList
	return MonComboScoreList

print("1v1 PROGRAM - Made by Mubs, version 0.1")
print("***************************************\n")

ProgramGen = input("Enter the generation in which this program is to import its matchups from: ")
ProgramIntCheck = 0

while(ProgramIntCheck != 1):
	if ((ProgramGen.isdigit()) == True):
		ProgramGen = int(ProgramGen)
		ProgramIntCheck = 1
	else:
		ProgramGen = input("\nYour previous response was not a number. Input a number: ")

if (ProgramGen <= 0 or ProgramGen > 8):
	MatchupStart = "test"
elif (ProgramGen == 1):
	MatchupStart = "rby"
elif (ProgramGen == 2):
	MatchupStart == "gsc"
elif (ProgramGen == 3):
	MatchupStart = "adv"
elif (ProgramGen == 4):
	MatchupStart = "dpp"
elif (ProgramGen == 5):
	MatchupStart = "bw"
elif (ProgramGen == 6):
	MatchupStart = "oras"
elif (ProgramGen == 7):
	MatchupStart = "sm"
elif (ProgramGen == 8):
	MatchupStart = "ss"
else:
	print("Unexpected error at ProgramGen.")

print("Set generation: " + MatchupStart)

MatchupFilePath = (MatchupStart + "matchups.txt")

SheetMatchupFile = open(MatchupFilePath, 'r')
SheetMatchups = SheetMatchupFile.read() 
ModifiedSheet = SheetMatchups.replace("\t", "\n")

SheetMatchupFile.close()

WriteFile = open('matchuplist.txt', 'w')
WriteFile.write(ModifiedSheet)
WriteFile.close() 

ProgramMatchupList = []

WriteFile = open('matchuplist.txt', 'r')
WriteLine = WriteFile.readline()
while(WriteLine):
	WriteLen = len(WriteLine)
	if (WriteLine.find("\n") > -1):
		WriteVar = WriteLen-1
		WriteReplace = str(WriteLine[:(WriteVar)])
		ProgramMatchupList.append(WriteReplace)
	WriteLine = WriteFile.readline()


ProgramIDList = []
ProgramSeedList = []

for item in ProgramMatchupList:
	if (item != 'm' and item != 'l' and item != 'w'):
		ProgramIDList.append(item)

for IDCounter in range (len(ProgramIDList)):
	ProgramSeedList.append(1 + random.random())

IDLen = len(ProgramIDList)
MatchupLen = len(ProgramMatchupList)
SheetLength = (int(MatchupLen / IDLen) - 1)

print("***************************************\n")
TeamMethod = input("Enter your choice of Teambuilding Method\n\nAvailible Options:\n1. One Pokemon Given\n2. Two Pokemon Given (FindThird)\n3. Random First Mon\n\nEnter the NUMBER listed for the option: ")
TeamMethodCheck = 0
while (TeamMethodCheck != 1):
	if ((TeamMethod.isdigit()) == True):
		TeamMethod = int(TeamMethod)
		if (TeamMethod >= 1 and TeamMethod <= 3):
			TeamMethodCheck = 1
		else:
			TeamMethod = input("\nThe NUMBER given was not a method listed. Please enter it again if it was a mistake\n\nAvailible Options:\n1. One Pokemon Given\n2. Two Pokemon Given (FindThird)\n3. Random First Mon\n\nEnter the NUMBER listed for the option: ")
	else:
		TeamMethod = input("\nYou did not enter a number. Please enter a number indicated by the '[NUMBER].' on the below options.\n\nAvailible Options:\n1. One Pokemon Given\n2. Two Pokemon Given (FindThird)\n3. Random First Mon\n\nEnter the NUMBER listed for the option: ")

OnePokemon = False
TwoPokemon = False
RandomChoice = False

if (TeamMethod == 1):
	OnePokemon = True
elif (TeamMethod == 2):
	TwoPokemon = True
elif (TeamMethod == 3):
	RandomChoice = True
	print("Selected Mode: Random Pokemon")

if (OnePokemon == True):
	print("Selected Mode: One Pokemon")
	print("***************************************\n")
	PokeChoiceList = [] 
	PokeChoiceLine = ""
	PokeList = [] 
	for countingpoke in range(1):
		PokeCheck = 0
		while (PokeCheck != 1):
			PokeAdd = input("Enter the first few letters of the Mon you want to use: ")
			PokeMod = PokeAdd.lower()
			PokeChar = len(PokeAdd)
			print(ProgramIDList)
			for item in ProgramIDList:
				if ((len(PokeChoiceList) <= 10) and (ProgramIDList.index(item) < IDLen - 1)):
					if (PokeMod == ((item[:PokeChar]).lower()) and len(PokeChoiceList) != 10):
						PokeChoiceList.append(item)
				else:
					for PokeCount in range (len(PokeChoiceList)):
						PokeChoiceLine = PokeChoiceLine +  str(PokeCount + 1) + ". " + PokeChoiceList[PokeCount] + "\n"
					PokeChoiceCheck = 0
					if (len(PokeChoiceList) != 0):
						PokeChoice = input("\nHere's a list of options that best fit what you put in. Choose the number of the choice in the Program that you would like to use:\n" +  PokeChoiceLine + "\nIf you want to CANCEL, use -1. ")
					else:
						print("Actually, Nothing in our index fits your search '" + PokeMod + "' try doing it again.\n")
						PokeChoiceList = [] 
						PokeChoiceLine = ""
						PokeChoiceCheck = 1
					while (PokeChoiceCheck != 1):
						if ((PokeChoice.isdigit()) == True or PokeChoice == "-1"):
							PokeChoice = int(PokeChoice)
							if (PokeChoice == -1):
								print("Choice Cancelled.")
								PokeChoiceCheck = 1
								PokeChoiceList = []
								PokeChoiceLine = ""
							elif (PokeChoice > 0 and PokeChoice <= (len(PokeChoiceList))):
								PokeChoiceFindIndex = PokeChoiceList[PokeChoice-1]
								PokeList.append(PokeChoiceFindIndex)
								PokeChoiceCheck = 1
								PokeChoiceList = []
								PokeLine = ""
								PokeCheck = 1
							else:
								MonChoice = input("\nThe Number you entered in is not in the range. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  PokeChoiceLine + "\nIf you want to CANCEL, use -1. ")
						else:
							MonChoice = input("\nWhat you put in is not a number. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  PokeChoiceLine + "\nIf you want to CANCEL, use -1. ")

if (TwoPokemon == True):
	print("Selected Mode: Two Pokemon")
	print("***************************************\n")
	Poke2ChoiceList = [] 
	Poke2ChoiceLine = ""
	Poke2List = []
	for countingpoke2 in range(2):
		Poke2Check = 0
		while (Poke2Check != 1):
			Poke2Add = input("Enter the first few letters of the Mon you want to use: ")
			Poke2Mod = Poke2Add.lower()
			Poke2Char = len(Poke2Add)
			for item in ProgramIDList:
				if ((len(Poke2ChoiceList) <= 10) and (ProgramIDList.index(item) < IDLen - 1)):
					if (Poke2Mod == ((item[:Poke2Char]).lower()) and len(Poke2ChoiceList) != 10):
						Poke2ChoiceList.append(item)
				else:
					for Poke2Count in range (len(Poke2ChoiceList)):
						Poke2ChoiceLine = Poke2ChoiceLine +  str(Poke2Count + 1) + ". " + Poke2ChoiceList[Poke2Count] + "\n"
					Poke2ChoiceCheck = 0
					if (len(Poke2ChoiceList) != 0):
						Poke2Choice = input("\nHere's a list of options that best fit what you put in. Choose the number of the choice in the Program that you would like to use:\n" +  Poke2ChoiceLine + "\nIf you want to CANCEL, use -1. ")
					else:
						print("Actually, Nothing in our index fits your search '" + Poke2Mod + "' try doing it again.\n")
						Poke2ChoiceList = [] 
						Poke2ChoiceLine = ""
						Poke2ChoiceCheck = 1
					while (Poke2ChoiceCheck != 1):
						if ((Poke2Choice.isdigit()) == True or Poke2Choice == "-1"):
							Poke2Choice = int(Poke2Choice)
							if (Poke2Choice == -1):
								print("Choice Cancelled.")
								Poke2ChoiceCheck = 1
								Poke2ChoiceList = []
								Poke2ChoiceLine = ""
							elif (Poke2Choice > 0 and Poke2Choice <= (len(Poke2ChoiceList))):
								Poke2ChoiceFindIndex = Poke2ChoiceList[Poke2Choice-1]
								Poke2List.append(Poke2ChoiceFindIndex)
								Poke2ChoiceCheck = 1
								Poke2ChoiceList = []
								Poke2ChoiceLine = ""
								Poke2Check = 1
							else:
								MonChoice = input("\nThe Number you entered in is not in the range. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  Poke2ChoiceLine + "\nIf you want to CANCEL, use -1. ")
						else:
							MonChoice = input("\nWhat you put in is not a number. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  Poke2ChoiceLine + "\nIf you want to CANCEL, use -1. ")

print("***************************************\n")
PromptMonsBeaten = input("Is there a set of Pokemon that you want to beat in your teams?\n1 for YES, 0 for NO: ")
PromptMonsBeatenCheck = 0
while (PromptMonsBeatenCheck != 1):
	if (PromptMonsBeaten.isdigit() == True):
		PromptMonsBeaten = int(PromptMonsBeaten) 
		if (PromptMonsBeaten == 1):
			MonsBeaten = True
			PromptMonsBeatenCheck = 1
		elif (PromptMonsBeaten == 0):
			MonsBeaten = False
			PromptMonsBeatenCheck = 1
		else:
			PromptMonsBeaten = input("\nThe Number you put in was neither 0 or 1. Again, if you want to input a list of Pokemon you want all the teams beat\n1 for YES, 0 for NO: ")
	else:
		PromptMonsBeaten = input("\nWhat you just inputted is not a number. Again, if you want to input a list of Pokemon you want all the teams beat\n1 for YES, 0 for NO: ")

if (MonsBeaten == True):
	print("***************************************\n")
	MonsList = []
	MonsChoiceList = []
	ChoiceLine = ""
	MonsListDone = False
	while (MonsListDone != True):
		MonAdd = input("Enter the first few letters of the Mon you want to beat\nor say STOP if you have all the Pokemon you want to beat: ")
		MonMod = MonAdd.lower()
		MonChar = len(MonAdd)
		if (MonMod != "stop"):
			for item in ProgramIDList:
				if ((len(MonsChoiceList) <= 10) and (ProgramIDList.index(item) < IDLen - 1)):
					if (MonMod == ((item[:MonChar]).lower()) and len(MonsChoiceList) != 10):
						MonsChoiceList.append(item)
				else:
					for BeatenCount in range (len(MonsChoiceList)):
						ChoiceLine = ChoiceLine +  str(BeatenCount + 1) + ". " + MonsChoiceList[BeatenCount] + "\n"
					MonChoiceCheck = 0
					if (len(MonsChoiceList) != 0):
						MonChoice = input("\nHere's a list of options that best fit what you put in. Choose the number of the choice in the Program that you would like to use:\n" +  ChoiceLine + "\nIf you want to CANCEL, use -1. ")
					else:
						print("Actually, Nothing in our index fits your search '" + MonMod + "' try doing it again.\n")
						ChoiceLine = ""
						MonsChoiceList = []
						MonChoiceCheck = 1
					while (MonChoiceCheck != 1):
						if ((MonChoice.isdigit()) == True or MonChoice == "-1"):
							MonChoice = int(MonChoice)
							if (MonChoice == -1 ):
								print("Choice Cancelled.")
								MonChoiceCheck = 1
								MonsChoiceList = []
								ChoiceLine = ""
							elif (MonChoice > 0 and MonChoice <= (len(MonsChoiceList))):
								ChoiceFindIndex = MonsChoiceList[MonChoice-1]
								MonsList.append(ChoiceFindIndex)
								MonChoiceCheck = 1
								MonsChoiceList = []
								ChoiceLine = ""
							else:
								MonChoice = input("\nThe Number you entered in is not in the range. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  ChoiceLine + "\nIf you want to CANCEL, use -1. ")
						else:
							MonChoice = input("\nWhat you put in is not a number. The number you need to input is before the point(.), ex: 1. metagross_1. Choose the number of the choice in the Program that you would like to use:\n" +  ChoiceLine + "\nIf you want to CANCEL, use -1. ")
		else:
			MonsListDone = True
			if (len(MonsList) == 0):
				MonsBeaten = False
			else:
				print("Your MonsBeaten: "  +  str(MonsList))

MonComboList = []
MonComboIDList = []
MonComboScoreList = []

if (OnePokemon == True):
	print("***************************************\n")
	mon1 = PokeList[0]
	monindex1 = ProgramIDList.index(mon1)
	mon1Find = ProgramMatchupList.index(mon1)
	mon1list = []
	for mcounter in range (SheetLength):
		mon1list.append(ProgramMatchupList[mon1Find + mcounter + 1])
	
	print("Processing Matchups.....")

	for moncounter1 in range (IDLen):
		for moncounter2 in range (IDLen):
			if (monindex1 != moncounter1 and moncounter1 != moncounter2 and monindex1 != moncounter2 and ((ProgramSeedList[monindex1] + ProgramSeedList[moncounter1] + ProgramSeedList[moncounter2]) in MonComboIDList) == False):
				MonComboIDList.append(ProgramSeedList[monindex1] + ProgramSeedList[moncounter1] + ProgramSeedList[moncounter2])
				mon2 = ProgramIDList[moncounter1]
				mon3 = ProgramIDList[moncounter2]
				mon2list = []
				mon3list = []
				MonResult = findscore(mon1, mon2, mon3)
				MonComboScoreList.append(MonResult)
				MonComboList.append(mon1 + " + " + mon2 + " + " + mon3)
elif (TwoPokemon == True):
	print("***************************************\n")
	mon1 = Poke2List[0]
	mon2 = Poke2List[1]
	monindex1 = ProgramIDList.index(mon1)
	monindex2 = ProgramIDList.index(mon2)
	mon1Find = ProgramMatchupList.index(mon1)
	mon2Find = ProgramMatchupList.index(mon2)
	mon1list = []
	mon2list = []
	for mcounter in range (SheetLength):
		mon1list.append(ProgramMatchupList[mon1Find + mcounter + 1])
		mon2list.append(ProgramMatchupList[mon2Find + mcounter + 1])
	print("Processing Matchups.....")

	for moncounter1 in range (IDLen):
		if (monindex1 != monindex2 and monindex2 != moncounter1 and monindex1 != moncounter1 and ((ProgramSeedList[monindex1] + ProgramSeedList[monindex2] + ProgramSeedList[moncounter1]) in MonComboIDList) == False):
			MonComboIDList.append(ProgramSeedList[monindex1] + ProgramSeedList[monindex2] + ProgramSeedList[moncounter1])
			mon3 = ProgramIDList[moncounter1]
			mon3list = []
			MonResult = findscore(mon1, mon2, mon3)
			MonComboScoreList.append(MonResult)
			MonComboList.append(mon1 + " + " + mon2 + " + " + mon3)
elif (RandomChoice == True):
	print("***************************************\n")
	mon1 = ProgramIDList[random.randint(0,(int(IDLen / 4)))]
	monindex1 = ProgramIDList.index(mon1)
	mon1Find = ProgramMatchupList.index(mon1)
	mon1list = []
	for mcounter in range (SheetLength):
		mon1list.append(ProgramMatchupList[mon1Find + mcounter + 1])
	print("Processing Matchups.....")

	for moncounter1 in range (IDLen):
		for moncounter2 in range (IDLen):
			if (monindex1 != moncounter1 and moncounter1 != moncounter2 and monindex1 != moncounter2 and ((ProgramSeedList[monindex1] + ProgramSeedList[moncounter1] + ProgramSeedList[moncounter2]) in MonComboIDList) == False):
				MonComboIDList.append(ProgramSeedList[monindex1] + ProgramSeedList[moncounter1] + ProgramSeedList[moncounter2])
				mon2 = ProgramIDList[moncounter1]
				mon3 = ProgramIDList[moncounter2]
				mon2list = []
				mon3list = []
				MonResult = findscore(mon1, mon2, mon3)
				MonComboScoreList.append(MonResult)
				MonComboList.append(mon1 + " + " + mon2 + " + " + mon3)

rearrangemaxvalue()

resultfile = open('result.txt', 'w')
monresultline = ""

for countingvar6 in range(len(MonComboScoreList)):
		monresultline = monresultline + (MonComboList[countingvar6] + "\n Score: " + str(MonComboScoreList[countingvar6]) + " ID: " + str(MonComboIDList[countingvar6]) + "\n")

resultfile.write(monresultline)

resultfile.close()

print("Done!\n")
print("***************************************\n")
print("Check results.txt for info.")