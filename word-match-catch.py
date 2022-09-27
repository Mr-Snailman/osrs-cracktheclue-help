# Thought process is that you can search for words from the free-to-play fish, remove them and there may be an anagram left over.
# Run command is: python word-match-catch.py

# Common words to search for in the clues.
dictionaryWords = [
    'FISH',
    'SHRIMP',
    'SARDINE',
    'HERRING',
    'ANCHOVIES',
    'SWORDFISH',
    'TUNA',
    'LOBSTER',
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
    print(searchDictionary(clueFullLines))
    print(searchDictionary(clueSections))

main()

