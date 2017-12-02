import os
import cv2
import numpy as np
from glob import glob
from generate_bitmap import generateLetterBitmap
import os


letters = open("Letters/mal_letters").read().split('\n')
fonts = glob("Fonts/ml/*.ttf")
out_path = 'Output/ml/'
size = 75*75

def generateLetter(fonts,character,size):
	letter_images = [generateLetterBitmap(font_path,character,size) for font_path in fonts]
	return letter_images
	
def generateAllLetters(letters,fonts,size,out_path):
	for letter in letters:
		letter_images = generateLetter(fonts,letter,size)
		letter_folder_path = out_path+'Item_'+letter+'/'
		os.mkdir(letter_folder_path)
		count = 0
		for img in letter_images:
			path = letter_folder_path+'Sample'+str(count)+'.jpg'
			count+=1
			cv2.imwrite(path,img)
			


generateAllLetters(letters,fonts,size,out_path)