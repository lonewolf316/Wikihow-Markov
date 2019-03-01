from wikipdf import pdfCreate
from pywikihow import WikiHow
import time, random, markovify

corpusCount = 10

allArticles = []

#Get data for x amount of articles
for i in range(0,corpusCount):
    randomWiki = WikiHow.random()
    allArticles.append(randomWiki)
    print("Got article: "+str(i+1))

print("Processing data and preparing to generate markov chains.")

#Extract the information from each article and combine to lists
titleList = ""
stepCounts = []
picList = []
stepList = ""
detailedList = ""

for article in allArticles:
    titleList = titleList + article["title"] + ". "
    stepCounts.append(len(article["steps"]))
    for step in article["steps"]:
        picList.append(step["pic"])
        stepList = stepList + step["step"] + " "
        detailedList = detailedList + step["detailed"]

#Pick number of steps, generate title
stepAmount = stepCounts[random.randint(0,len(stepCounts)-1)]
titleModel = markovify.Text(titleList, state_size=1)
finalTitle = titleModel.make_sentence()

#initialize list and markov chains for generation
steps=[]
stepModel = markovify.Text(stepList, state_size=1)
detailedModel = markovify.Text(detailedList, state_size=2)
for step in range(0,stepAmount):
    steps.append({})

    #Generate step
    while True:
        stepText = stepModel.make_sentence()
        if stepText != None:
            break
    steps[step]["step"] = stepText

    #Generate step details
    fullDetailed = ""
    for x in range(0,5):
        while True:
            detailedText = detailedModel.make_sentence()
            if detailedText != None:
                break
        fullDetailed += " " + detailedText
    steps[step]["detailed"] = fullDetailed

    stepImg = picList[random.randint(0,len(picList)-1)]
    steps[step]["pic"] = stepImg

pdfCreate(finalTitle, steps)