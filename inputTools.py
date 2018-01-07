
import sys,csv
import pandas as pd
import numpy as np

from userData import user
from sklearn import datasets

class userDataStruct():
    userData = ""
    likesData = ""
    featureData = ""
    textData = 0

def sampleInput(inputFile):
    
    inputFilePro = inputFile + "/profile/profile.csv"
    
    csvReader = csv.reader(open(inputFilePro))
    
    count = 0
    users = []
    
    for row in csvReader:
        
        if count == 0:
            count = count+1
            continue
        
        parameterSplit = ','.join(row)
        parameters = parameterSplit.split(',')
        
        singleUser = user(1)
        singleUser.id = parameters[1]
        singleUser.age = float(parameters[2])
        singleUser.genderType = float(parameters[3])
        singleUser.open = float(parameters[4])
        singleUser.conscientious = float(parameters[5])
        singleUser.extrovert = float(parameters[6])
        singleUser.agreeable = float(parameters[7])
        singleUser.neurotic = float(parameters[8])
                
        user.idList.append(parameters[1])
        users.append(singleUser)
        
        print(len(users))
    
    inputFileRel = inputFile + "/relation/relation.csv"
    
    csvReader = csv.reader(open(inputFileRel))
    count = 0
    userID = -1
    '''
    for row in csvReader:
        
        if count == 0:
            count = count+1
            continue       
        
        parameterSplit = ','.join(row)
        parameters = parameterSplit.split(',')
                               
        userID = parameters[1]
        print(parameters[1])
        users[user.idList.index(userID)].likeID.append(parameters[2])
    
    '''
    return users

def userInput(inputFile):
    
    inputFilePro = inputFile + "/profile/profile.csv"
    
    csvReader = csv.reader(open(inputFilePro))
    
    count = 0
    users = []
    
    for row in csvReader:
        
        if count == 0:
            count = count+1
            continue
        
        parameterSplit = ','.join(row)
        parameters = parameterSplit.split(',')
        
        singleUser = user(1)
        singleUser.id = parameters[1]
        user.idList.append(parameters[1])
        users.append(singleUser)
    
    
    inputFileRel = inputFile + "/relation/relation.csv"
    
    csvReader = csv.reader(open(inputFileRel))
    count = 0
    userID = -1
    for row in csvReader:
        
        if count == 0:
            count = count+1
            continue       
        
        parameterSplit = ','.join(row)
        parameters = parameterSplit.split(',')
                               
        userID = parameters[1]
        users[user.idList.index(userID)].likeID.append(parameters[2])
    
    return users

def sampleInputPd(inputFile):
    userDF = userDataStruct()
    userDF.userData = pd.read_csv(inputFile+"/profile/profile.csv")
    userDF.likesData = pd.read_csv(inputFile+"/relation/relation.csv")
    userDF.featureData = pd.read_csv(inputFile+"/LIWC/LIWC.csv")
    userDF.textData = datasets.load_files(inputFile,load_content=True,categories='text')
    
    return userDF


    
    
    
    