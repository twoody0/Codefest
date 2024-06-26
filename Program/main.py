#!/usr/bin/env python
import Classification
import PreProcess
import UserInput


def main():
    print("Welcome to our data set predictor!")
    fileName = UserInput.getFileName()
    originalFile = UserInput.openFile(fileName)
    guessColumn = UserInput.getGuessColumn(originalFile,fileName)
    colRemovedFile = UserInput.removeColumns(originalFile,fileName,guessColumn)
    processedFile = PreProcess.processFile(colRemovedFile)
    dataType = UserInput.getGuessType()
    results = Classification.pickClassification(processedFile, guessColumn,dataType)
    # print(results)
    if dataType == 'continuous':
        Classification.printAcurracy(results)
        Classification.plotModelDiagnostics(results[0],results[1])
    else:
        Classification.printKnnAccuracy(results[0], results[1])
        Classification.plotKnnAccuracy(results[0],results[1])

if __name__ == "__main__":
    main()