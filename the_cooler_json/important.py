def this_wrap(f):
 def wrapper(self,*args,**kwargs):f.__globals__.update({"this":self});ret=f(*args,**kwargs);return ret
 return wrapper
def self_wrap(f):
  def wrapper(self,*args,**kwargs):f.__globals__.update({"self":self});ret=f(*args,**kwargs);return ret
  return wrapper
class JS(type):
 def __new__(cls,name,bases,dct):
  for v in dct:
   if callable(dct[v]):dct[v]=this_wrap(dct[v]) if not v.endswith("_erm_actually_its_self") else self_wrap(dct[v])
  x = super().__new__(cls,name,bases,dct);return x
try:
    class Made:a=1
    raise False
except:
    class MadeByMe(Made,BaseException,metaclass=JS):b=2
    @lambda r:False
    class true:100
    @(lambda v:lambda k:v)(True)
    class false:200
finally:"";someimportantvariablethatisverylong=[0,9,8,7,6,5,4,3,2,1];someimportantvariablethatisvery1ong=[0O2,34,6,4,23,2,12,3,6,34];import threading as th
class th(th.Thread):ok=0;setit=lambda x:setattr(x,'ok',1);__init__=lambda m,i:super().__init__(target=lambda:not i() and m.setit())