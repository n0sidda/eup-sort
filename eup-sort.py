import os
import shutil
import time
#config options
modelType = 'mp_f_freemode_01'
modelSubType = 'jbib' #jbib, lowr, decl, teef, etc
EUPDirectory = '' #directory that contains your giant list of .ydd's and .ytds in a single folder
logFile = 'log.txt'
yddPosiAdd = 0
ytdPosiAdd = 0
# Automatic adjustment dependent on if modelSubType is a component or prop
if (len(modelSubType) == 4):
    yddPosiAdd = 6
    ytdPosiAdd = 11
else:
    yddPosiAdd = 8
    ytdPosiAdd = 13

os.chdir(EUPDirectory)

yddArray = []
ytdArray = []

#f = open(logFile, 'a')
for file in os.listdir():
    if (file.find('.ydd') != -1 and file.find(modelType) != -1 and file.find(modelSubType) != -1):
        yddArray.append(file)
        #f.write(file + "\n")
    elif (file.find('.ytd') != -1 and file.find(modelType) != -1 and file.find(modelSubType) != -1):
        ytdArray.append(file)
        #f.write(file + "\n")

#print(ytdArray)
#print(yddArray)


#test stuff
currentModel = 0
for model in yddArray:
    
    currentTexture = 0
    currentYDD = yddArray[currentModel]
    dlcIdentifierYDD = currentYDD[:currentYDD.find('^')]
    numberIdentifierYDD = currentYDD[currentYDD.find('^')+yddPosiAdd:currentYDD.find('.')]
    matchingYTDs = []
    #Create appropriate folder for YTD
    createdDirectory = EUPDirectory + '\\' + str(currentModel)
    os.mkdir(createdDirectory)
    shutil.copyfile(EUPDirectory + '\\' + currentYDD, EUPDirectory + '\\' + str(currentModel) + '.ydd')


    for texture in ytdArray:
        dlcIdentifierYTD = texture[:texture.find('^')]
        numberIdentifierYTD = texture[texture.find('^')+ytdPosiAdd:texture.find('.')]
        
        afterCarrot = texture[texture.find('^'):]
        print(model + ' compared to ' + texture + '\n')

        print(afterCarrot[:4])
        if (dlcIdentifierYDD == dlcIdentifierYTD and numberIdentifierYDD[:3] == numberIdentifierYTD[:3] and afterCarrot[1:5] == modelSubType):
            #print('made it here')
            print(dlcIdentifierYDD + '\n' + numberIdentifierYDD + '\n' + dlcIdentifierYTD + '\n' + numberIdentifierYTD + '\n')
            matchingYTDs.append(texture)
            #print(currentYDD)
            print(model + ' was matched with ' + texture + '\n')

    for match in matchingYTDs:
        print()
        shutil.copyfile(EUPDirectory + '\\' + match, createdDirectory + '\\' + str(currentTexture) + '.ytd')
        currentTexture += 1

    matchingYTDs.clear()
    currentModel +=1
