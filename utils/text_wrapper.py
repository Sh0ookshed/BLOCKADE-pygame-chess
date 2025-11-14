#------------------------------------------------------------------------------
#TEXT WRAPPER
#------------------------------------------------------------------------------

#Function that wraps text inside pygame rect objects. Needed for Display boxes / Buttons / Dropdowns 
#if text ever starts to get a bit large.

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#text wrap function
#------------------------------------------------------------------------------

def text_wrap(text, font, width):
    width = width - 10
    split_text = text.split(" ")
    text_lines = []
    line = ""

    for word in split_text:
        
        if  font.size(line + word + " ")[0] <= width:

            if split_text[len(split_text)-1] == word:
                line = line + word

            else:
                line = line + word + " "

        else:
            text_lines.append(line.strip())
            line =  word + " "

    if line.strip():
        text_lines.append(line.strip())

    return text_lines