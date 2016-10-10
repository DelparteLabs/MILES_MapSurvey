#from json import load, JSONEncoder
from optparse import OptionParser
from re import compile
import os
import io
import json

path = "C:/Data/Website/PokeyMap/data/merg/"
##float_pat = compile(r'^-?\d+\.\d+(e-?\d+)?$')
##charfloat_pat = compile(r'^[\[,\,]-?\d+\.\d+(e-?\d+)?$')
##defaults = dict(precision=6)
##parser.set_defaults(**defaults)
##parser.add_option('-p', '--precision', dest='precision', type='int', help='Digits of precision, default %(precision)d.' % defaults)

lst = os.listdir(path)

outjson = dict(type='FeatureCollection', features=[])
for infile in lst:
    print infile
    injson = json.load(open(path+infile))

    outjson['features']+=injson['features']

encoder = json.JSONEncoder(separators=(',', ':'))
encoded = encoder.iterencode(outjson)
#format = '%.' + str(options.precision) + 'f'
with open("C:/Data/Website/PokeyMap/data/allcomments.json", 'w') as outf:
    json.dump(outjson, outf)

##for token in encoded:
##        if charfloat_pat.match(token):
##            # in python 2.7, we see a character followed by a float literal
##            output.write(token[0] + format % float(token[1:]))
##
##        elif float_pat.match(token):
##            # in python 2.6, we see a simple float literal
##            output.write(format % float(token))
##
##        else:
##            output.write(token)

