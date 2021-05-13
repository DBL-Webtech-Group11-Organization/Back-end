import numpy as np

#The python file for all the functions for the different visualizations
import pandas as pd


def makeGraphs():
    pass

def makeMatrix(data):
    #We have to first find how many ID's we have in the file
    largestID = 0
    for i in range(len(data)):
        if data[i][1] > largestID:
            largestID = data[i][1]
    #Create a 2-multidimensional array with the largestID length and set correct ID number to every column and row
    mailMatrix = np.zeros((largestID,largestID),dtype=int)
    for i in range(len(mailMatrix)):
        mailMatrix[0][i] = i
        mailMatrix[i][0] = i

    #Count how often any id send an email to another ID
    for i in range(1,largestID):
        for j in range(len(data)):
            if i == data[j][1]:
                mailMatrix[data[j][4] - 1][i - 1] += 1


    return mailMatrix


