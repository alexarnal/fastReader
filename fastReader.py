import matplotlib.pyplot as plt
from PIL import Image

#Read file
fileName = 'Research/Readings/test.txt'
file = open(fileName, "r")
content = file.readlines()

#Turn file into a single string
string = ''
for line in content:
    string+=line.replace('\n', ' ')

#Break string into individual words
words = string.split(" ")

#Use this code to figure out which fontsize to use
longest = 0
size = 0
ind = 0
for i,word in enumerate(words):
    if size < len(word):
        longest = word
        size = len(word)
        ind = i 
fs=35
plt.text(0.5,0.5, words[i], fontsize=fs, ha='center', va='center')
plt.axis('off')
        
#Save all words as individual images
for i,word in enumerate(words):
    plt.text(0.5,0.5, words[i], fontsize=fs, ha='center', va='center')
    plt.axis('off')
    plt.savefig('Research/Readings/test %s.png'%i)
    plt.clf()

#Read all saved images into a list
images = []
for i in range(len(words)):
    images.append(Image.open('Research/Readings/test %s.png'%i))
 
#Make gif that loops once
images[0].save('Research/Readings/test.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=200, loop=1)