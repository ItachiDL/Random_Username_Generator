import re
def fileFormating(file):
    with open(file, 'r') as f:
        content = f.read()
        f.close()
        return content
    
def fileWriting(file, content):
    with open(file, 'w') as f:
        for word in content:
            f.write(word.strip() + '\n')
        
        
content = fileFormating("locations.txt")
split = content.split('\n')
wordList = []
for word in split:
    cleanedText = re.sub(r'[^A-Za-z0-9]', '', word)
    wordList.append(cleanedText)
fileWriting("locations.txt", wordList)

