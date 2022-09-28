# Run command is: python word-match-catch.py

import pprint
import string
    
pp = pprint.PrettyPrinter(depth=3)

# Thought process is that you can search for words from the free-to-play fish, remove them and there may be an anagram left over.
# Common words to search for in the clues.
fishWords = [
    'FISH',
    'ANCHOVIES',
    'HERRING',
    'LOBSTER',
    'PIKE',
    'SALMON',
    'SARDINE',
    'SHRIMP',
    'SWORDFISH',
    'TROUT',
    'TUNA',
    'NET',
    'ROD',
    'POT'
]

# Search for Common Locations
locations = [
    'ALKHARID',
    'FALADOR',
    'LUMBRIDGE',
    'VARROCK',
    'RIMMINGTON',
    'PORTSARIM',
    'SARIM',
    'WILDERNESS',
    'MONASTERY',
    'DRAYNOR',
    'DRAYNORMANOR',
    'DRAYNORVILLAGE',
    'CRAFTING',
    'CRAFTINGGUILD',
    'MELZAR',
    'MELZARSMAZE',
    'CHAMPIONSGUILD',
    'DUELARENA',
    'CITHAREDEABBEY',
    'CITHAREDE',
    'COOKSGUILD',
    'GRANDEXCHANGE',
    'LUMBERYARD',
    'ICEMOUNTAIN',
    'BLACKKNIGHTFORTRESS',
    'BLACKKNIGHT',
    'GOBLINVILLAGE',
    'FARM'
]

# Represents the FULL line of the clue, Left and Right side
clueFullLines = [
    'YPWAIETOAENRMHMGENMIVWDMKDTCBANGBFKW',
    'NQLLWQMIRLVFSDROTNVKIIAAKIRLHADHESVG',
    'LINVADMCURYBOFEUAIDRULRHTDEESEBREPYE',
    'VRBOOHHSDEWEAANANNEERATOLITEJEPEPZFN',
    'ANHIITBICPATELTTMHFEKETCHPMSNAFEWNQM',
    'SFTOAINWLXARKLANFENEWEDSANENTEGQLHUA',
    'OENIRSRONOFKGVEKARTLBGONGUWHILPAFNAS',
    'EHERESSOVEMDGJTCWSRDMCORRODAPJNLSAWY',
    'TASEWNHEVGRANOKNOTSHTOELHTICUTMLHOIO',
    'HRFRONLRATTATTIQATANEUOASGNHSFALEHND'
]

# Represents the Split lines individually
clueSections = [
    'YPWAIETOAENRMHMGEN',
    'NQLLWQMIRLVFSDROTN',
    'LINVADMCURYBOFEUAI',
    'VRBOOHHSDEWEAANANN',
    'ANHIITBICPATELTTMH',
    'SFTOAINWLXARKLANFE',
    'OENIRSRONOFKGVEKAR',
    'EHERESSOVEMDGJTCWS',
    'TASEWNHEVGRANOKNOT',
    'HRFRONLRATTATTIQAT',
    'MIVWDMKDTCBANGBFKW',
    'VKIIAAKIRLHADHESVG',
    'DRULRHTDEESEBREPYE',
    'EERATOLITEJEPEPZFN',
    'FEKETCHPMSNAFEWNQM',
    'NEWEDSANENTEGQLHUA',
    'TLBGONGUWHILPAFNAS',
    'RDMCORRODAPJNLSAWY',
    'SHTOELHTICUTMLHOIO',
    'ANEUOASGNHSFALEHND'
]

clueBetweenII = ['TBICPATELTTMHSFTOAINWLXARKLANFEOENIRSRONOFKGVEKAREHERESSOVEMDGJTCWSTASEWNHEVGRANOKNOTHRFRONLRATTATTIQATMIVWDMKDTCBANGBFKWVK']

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

matrix = transpose(clueFullLines)
clueTransposed = []
for i in range(len(matrix)):
    clueTransposed.append(''.join(matrix[i]))

def searchDictionary(dictionary, clueLines):
    results = {}
    # For each Line of the clue...
    for line in clueLines:
        # For each Word in our small dictionary...
        for word in dictionary:
            wordMatch = True
            lineAfter = line
            # For each character in the Word from the dictionary...
            for character in word:
                # Check if it exists in the given line of the clue; if so, remove it and keep processing.
                # Otherwise, skip to the next Word. Keep track of remaining letters.
                if character in lineAfter:
                    lineAfter = lineAfter.replace(character, "", 1)
                else:
                    wordMatch = False
                    break

            # Create a Tuple of the word that was matched to the remaining letters.
            # Store via the original clue line for ease of seeing/tracking where it came from.
            if wordMatch:
                if line in results.keys():
                    results[line].append( (word, lineAfter) )
                else:
                    results[line] = [ (word, lineAfter) ]

    return results

# TODO: This only searches front of the dictionary and removes as it goes; want to do a N*N algorithm to search by each combination of words
def searchDictionaryFullLine(dictionary, clueLines):
    results = {}
    # For each Line of the clue...
    for line in clueLines:
        lineAfter = line
        # For each Word in our small dictionary...
        for word in dictionary:
            wordMatch = True
            # For each character in the Word from the dictionary...
            for character in word:
                # Check if it exists in the given line of the clue; if so, remove it and keep processing.
                # Otherwise, skip to the next Word. Keep track of remaining letters.
                if character not in lineAfter:
                    wordMatch = False
                    break

            # Create a Tuple of the word that was matched to the remaining letters.
            # Store via the original clue line for ease of seeing/tracking where it came from.
            if wordMatch:
                for character in word:
                    lineAfter = lineAfter.replace(character, "", 1)

                if line in results.keys():
                    results[line].append( (word, lineAfter) )
                else:
                    results[line] = [ (word, lineAfter) ]

    return results

def searchFishWords(clueLines):
    return searchDictionary(fishWords, clueLines)

def searchLocations(clueLines):
    #return searchDictionary(locations, clueLines)
    return searchDictionaryFullLine(locations, clueLines)

def fishSearch():
    pp.pprint(searchFishWords(clueFullLines))
    pp.pprint(searchFishWords(clueSections))
    #pp.pprint(searchFishWords(clueTransposed))
    #pp.pprint(searchFishWords(clueBetweenII))

def locationSearch():
    pp.pprint(searchLocations(clueFullLines))
    pp.pprint(searchLocations(clueSections))
    #pp.pprint(searchLocations(clueTransposed))
    pp.pprint(searchLocations(clueBetweenII))


def skipEveryOtherLetter(isOdd, clueLines):
    everyOtherLetterLine = []
    for line in clueLines:
        skipLine = ''
        for i in range(len(line)):
            if (isOdd and i % 2 == 1) or (not isOdd and i % 2 == 0):
                skipLine += line[i]
        everyOtherLetterLine.append(skipLine)
    return everyOtherLetterLine

def skipEveryOtherCheckOdd():
    pp.pprint(skipEveryOtherLetter(True, clueFullLines))
    pp.pprint(skipEveryOtherLetter(True, clueSections))
    #pp.pprint(skipEveryOtherLetter(True, clueTransposed))
    pp.pprint(skipEveryOtherLetter(True, clueBetweenII))

def skipEveryOtherCheckEven():
    pp.pprint(skipEveryOtherLetter(False, clueFullLines))
    pp.pprint(skipEveryOtherLetter(False, clueSections))
    #pp.pprint(skipEveryOtherLetter(False, clueTransposed))
    pp.pprint(skipEveryOtherLetter(False, clueBetweenII))

def twoLetterModular(clueLines):
    alphabet = string.ascii_uppercase
    newLines = []
    for line in clueLines:
        newLine = ''
        for i in range(0, len(line) - 1, 2):
            newLine += alphabet[(alphabet.index(line[i]) + alphabet.index(line[i+1])) % len(alphabet)]
        newLines.append(newLine)
    return newLines

def checkTwoLetterModular():
    pp.pprint(twoLetterModular(clueFullLines))
    pp.pprint(twoLetterModular(clueSections))
    pp.pprint(twoLetterModular(clueBetweenII))

def main():
    #fishSearch()
    #locationSearch()
    #skipEveryOtherCheckOdd()
    #skipEveryOtherCheckEven()
    checkTwoLetterModular()

main()

