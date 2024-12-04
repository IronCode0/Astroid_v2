
from lib import debug as dg


global dc
def c():
    dg.cout("hello")
    dg.cout("hello",7858)
    dg.cout("hello",trace=True)
    dg.cout([7,"fefe"])
    dg.cout(["hello","fefe"],7858)
    dg.cout(["hello","fefe"],trace=True)
    dg.cout({1:"hello","ll":"jviueiue"})
    dg.cout({1:"hello","ll":"jviueiue"},7858)
    dg.cout({1:"hello","ll":"jviueiue"},trace=True)

def d(): c()
def e(): d()
e()