import xml.etree.ElementTree as ET
import pandas as pd
import time

def getTracksFromXML(xmlFile):
    """XML File => list of XML dicts"""
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    mainDict = root.findall('dict')
    
    for item in list(mainDict[0]):
        if item.tag=='dict':
            tracksDict = item
            break
    trackList = list(tracksDict.findall('dict'))
    tracksList = []
    for item in trackList:
        tracksList.append(list(item))
    
    return tracksList

def tracksAsLists(xmlDicts):
    """List of XML Dicts => list of XML elements"""
    tracksList = []
    for item in xmlDicts:
        tracksList.append(list(item))
    return tracksList

def createDF(xmlFile, cols):
    """list of XML elements => Dataframe"""
    trackDicts = getTracksFromXML(xmlFile)
    trackListXML = tracksAsLists(trackDicts)

    df = pd.DataFrame(columns = cols)
    dict = {}
    for i in range(len(trackListXML)):
        for j in range(len(trackListXML[i])):
            if trackListXML[i][j].tag == 'key':
                if trackListXML[i][j].text not in cols:
                    continue
                dict[trackListXML[i][j].text] = trackListXML[i][j+1].text         
        listKeys = [i for i in dict.keys()]
        listVals = [j for j in dict.values()]
        dfTemp = pd.DataFrame([listVals], columns = listKeys)
        df = pd.concat([df, dfTemp], axis = 0, ignore_index = True, sort = True)
        print(f'Track {i+1} of {len(trackListXML)}')
    return df

def compareWeeklyDFs(dfLastWeek, dfThisWeek):
    """df1, df2 => df3"""
    dfOut = dfThisWeek.copy()
    dfOut['Play Count'] = dfThisWeek['Play Count'].astype(int) - dfLastWeek['Play Count'].astype(int)
    dfOut = dfOut[dfOut['Play Count'] != 0]
    dfOut['Play Count'].fillna(dfThisWeek['Play Count'], inplace = True)
    dfOut['Play Count'] = dfOut['Play Count'].astype(int)

    return dfOut



# The columns I am interested in comparing week-by-week
cols = ['Track ID', 'Name', 'Artist', 'Album', 'Total Time',
        'Date Added', 'Play Count']

df1 = createDF('Library09_21_23.xml', cols)
df2 = createDF('Library09_22_23.xml', cols)
df3 = compareWeeklyDFs(df1, df2)
df3.sort_values(by=['Play Count'], ascending=False, inplace=True)
df3.reset_index(inplace = True)

fileTitle = time.strftime('%y_%m_%d')
fileTitle = fileTitle + 'Listening.csv'

df3.to_csv(fileTitle)
