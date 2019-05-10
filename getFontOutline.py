import json
import os
import sys
from fontTools.pens.recordingPen import RecordingPen
from fontTools.ttLib import TTFont

def getGlyph(glyphSet, cmap, char):
    name = cmap[ord(char)]
    return glyphSet[name]

def traceFont(font, char):    
    glyphSet = font.getGlyphSet()
    cmap = font.getBestCmap()
    glyph = getGlyph(glyphSet, cmap, char)
    recordingPen = RecordingPen()
    glyph.draw(recordingPen)
    return recordingPen.value

def traceStr(font, str):
    penValue = []
    for c in str:
        penValue.append(traceFont(font, c))
    return penValue

def validate(args):
    usage = 'Usage: python {} FILE characters [-o]'\
            .format(__file__)
    if len(args) == 1:
        print(usage)
        return False
    return True

def getPath():
    path = os.path.dirname(__file__)
    if len(path) >= 1:
        path += '/'
    return path

def getFontPath():
    return getPath() + 'font/SourceHanSans-Light.otf'

def getOutputPath(filename):
    return  getPath() + 'output/' + filename


args = sys.argv
if not validate(args):
    exit()
str = args[1]

font = TTFont(getFontPath())
penValue = traceStr(font, str)
jv = json.dumps(penValue, ensure_ascii=False)

if len(args) >= 3 and args[2] == '-o':
    with open(getOutputPath(str + '.json'), 'w') as f:
        print(jv, file=f)
else:
        print(jv)