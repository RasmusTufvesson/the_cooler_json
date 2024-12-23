import sys, json
import os.path as f
c = f.dirname
class f: c = c
def importit(what, whatsit):
    from . import important
    what.update(important.__dict__)
f.k = importit
del f.c
def buteye_dont_understand(toks, p):
    p.__init__=json.loads("".join([{8:"0",7:"1",5:"3",4:"4",1:"2",2:"5",3:"6",6:"7",0:"8",9:"9",23:'"'}.get(j,chr(j))for j in toks]))
f.i = sys
sys.modules[__name__]=(f,buteye_dont_understand,)