# Thought process is that you can search for words from the free-to-play fish, remove them and there may be an anagram left over.
# Run command is: python word-match-catch.py

import pprint

# Common words to search for in the clues.
dictionaryWords = [
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

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

matrix = transpose(clueFullLines)
clueTransposed = []
for i in range(len(matrix)):
    clueTransposed.append(''.join(matrix[i]))

def searchDictionary(clueLines):
    results = {}
    # For each Line of the clue...
    for line in clueLines:
        # For each Word in our small dictionary...
        for word in dictionaryWords:
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

def main():
    pp = pprint.PrettyPrinter(depth=3)
    pp.pprint(searchDictionary(clueFullLines))
    pp.pprint(searchDictionary(clueSections))
    pp.pprint(searchDictionary(clueTransposed))

main()

