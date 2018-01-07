import sys,getopt,random

import pandas as pd
import numpy as py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import feature_selection,preprocessing,linear_model
from sklearn.svm.classes import LinearSVR, LinearSVC


from inputTools import userInput
from inputTools import sampleInput
from outputTools import outputResult
import learningTools as lt
import inputTools
from userData import user


if __name__ == '__main__':
    
    opts,args = getopt.getopt(sys.argv[1:], "i:o:")
    inputFile = ""
    outputFile = ""
    trainingFile = 'data/training'
    
    for op,value in opts:
        if op == "-i":
            inputFile = value
            print(inputFile)
        if op == "-o":
            outputFile = value
            print(outputFile)
    
    userDF = inputTools.sampleInputPd(trainingFile)
    vectorizerG = CountVectorizer()
    vectorizerA = CountVectorizer()
    
    
    clfAge = lt.likesIDAgeMNB(userDF,vectorizerA)
    clfGender = lt.likesIDGenderMNB(userDF,vectorizerG)
    #clfAge = lt.LIWCAgegroupSVM(userDF)
    #clfGender = lt.LIWCGenderSVM(userDF,vectorizerG)
    
    clfPersonality  = []
    selectors = []
    scalerX = preprocessing.Normalizer(norm='l2')
    features = ['ope','con','ext','agr','neu']
    featureSize = [40,40,40,40,40]
    costs = [1,1,1,1,1]
    ga = [0.0001,0.0001,0.00001,0.0001,'auto']    
    
    userDF.featureData.rename(columns={'userId':'userid'},inplace=True)
    userFeature = pd.merge(userDF.featureData,userDF.userData,on='userid',how= 'right')
    
    i=0
    for feature in features:
        
        '''selector = feature_selection.SelectKBest(score_func=feature_selection.f_regression
                                                 ,k=featureSize[i])'''
        

        clff = LinearSVR(loss='squared_epsilon_insensitive',C=costs[i])
        
        X = userFeature.ix[:,'WC':'AllPct']
        X = scalerX.transform(X)
        
        #print(userDF.userData)

        y =userFeature.ix[:,feature]
        
        lars_cv = linear_model.LassoLarsCV(cv=6).fit(X,y)
        selector = feature_selection.SelectFromModel(lars_cv,prefit=True)
        
        X = selector.transform(X)
        
        selectors.append(selector)
        print(feature)
        print(X.shape)
        print(y.shape)
        clff.fit(X,y)
        
        clfPersonality.append(clff)
        i=i+1
    
    
    samples = inputTools.sampleInputPd(inputFile)
    
    lt.predictAgeLikesid(samples, clfAge, vectorizer= vectorizerA)
    lt.predictGenderLikesid(samples, clfGender,vectorizer= vectorizerG)
    

    samples.featureData.rename(columns={'userId':'userid'},inplace=True)
    personalityData = pd.merge(samples.featureData,samples.userData,on='userid',how= 'right')
    
    
    #samples.userData['age_group'] = 0
    #samples.userData['age_group'] = clfAge.predict(X)
    
    #samples.userData['gender'] = clfGender.predict(X)
    
    i=0
    
    for feature in features:
        
        X = personalityData.ix[:,'WC':'AllPct']
        X = scalerX.transform(X)
        X = selectors[i].transform(X)
        
        print(feature)
        print(X.shape)
        
        personalityData[feature] = clfPersonality[i].predict(X)
        i += 1
    
    
    
    for index,rows in personalityData.iterrows():
        
        singleUser = user(0)
        
        singleUser.id = personalityData.loc[index,'userid']
        
        if personalityData.loc[index,'age_group'] == 1:
            singleUser.age_group = "xx-24"
        if personalityData.loc[index,'age_group'] == 2:
            singleUser.age_group = "25-34"
        if personalityData.loc[index,'age_group'] == 3:
            singleUser.age_group = "35-49"
        if personalityData.loc[index,'age_group'] == 4:
            singleUser.age_group = "49-xx"
        
        
        if personalityData.loc[index,'gender'] == 1:
            singleUser.gender = "female"
        else:
            singleUser.gender = "male"
        
        singleUser.open=personalityData.loc[index,'ope']
        singleUser.conscientious=personalityData.loc[index,'con']
        singleUser.extrovert=personalityData.loc[index,'ext']
        singleUser.agreeable=personalityData.loc[index,'agr']
        singleUser.neurotic=personalityData.loc[index,'neu']
            
        outputResult(singleUser,outputFile)
    

        
    
    
    