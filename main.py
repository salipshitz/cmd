from os import system
import sys
from importlib import import_module

sys.tracebacklimit = None

def excepthook(err, value, tb):
    err = repr(err).split("'")
    err = err[1]
    err = err.split('.')
    if len(err) > 1:
        err = err[1]
    else:
        raise CompilerE
        err = err[0]
    if str(value) not in (None, ''):
        print(err, value, sep=': ')
    else:
        print(err, value.__doc__, sep=': ')

sys.excepthook = excepthook

class BaseE(Exception):
    """Base class for errors"""

class CompilerE(BaseE):
    """Compiler failed"""

class SyntaxE(BaseE):
    """Invalid syntax."""

class NameE(BaseE):
    """Name does not exist"""

meth = {}
clas = {}

def replace(text, char, withChar):
    text = text.split(char)
    return withChar.join(text)

def runfunc(nm, args):
    code = var[nm]["code"]
    fargs = var[nm]["args"]
    i = 0
    codelns = code.splitlines()
    while i < len(codelns):
        compiler.compilecode(codelns[i])
        i += 1

def newfunc(nm, *args):
    code = ""
    while True:
        code += "\n"+input("")
        if code.endswith("}"):
            code = code[:-1]
            break
    var[nm] = {"args": args, "code": code}

def newclass(nm, *args):
    code = ""
    while True:
        code += "\n"+input("")
        if code.endswith("}"):
            code = code[:-1]
            break
    if var[nm] != None:
        del var[nm]
    clas[nm] = {"args": args, "init": code, "meths": {}, "inst": []}

def newmeth(clas_, nm, *args):
    code = ""
    while True:
        code += "\n"+input("")
        if code.endswith("}"):
            code = code[:-1]
            break
    clas[clas_]["meths"][nm] = {"args": args, "code": code}

def switch(thing):
    conds = {}
    default = ''
    while True:
        cond = input("")
        assert(cond.endswith("{"))
        cond = cond[:-1]
        code = ""
        while True:
            code += '\n'+input("\t")
            if code.endswith("}"):
                code = code[:-1]
                break
        if cond == 'default':
            default = code
        else:
            conds[cond] = code
            
def init(clas_, *args):
    code = clas[clas_]["init"]
    fargs = var[clas_]["args"]
    i = 0
    codelns = code.splitlines()
    clas[clas_]["inst"] += {"var": {}}
    while i < len(codelns[i]):
        cd = codelns[i].split(".")
        if codelns[i].split(".") == "THIS":
            del cd[0]
            cd = ".".join(cd)
            cd = code.split(" ")
            cd[0] = "clas[{!r}]['inst']['var'][{!r}]".format(clas_, cd[0])
        compiler.compilecode(codelns[i])
        i += 1

def echo(*args, sep=' ', end='\n'):
    for i, arg in enumerate(args):
        args[i] = str(arg)
    text = ""
    for arg in args:
        text += arg
        if arg is not arg[-1]:
            text += sep
        else:
            text += end
    print(text, end='')
    return text

def end():
    exit()

def clear():
    system('cls')

def get_module(module):
    mod = import_module(module)
    meth += mod.meth

def raiseE(E):
    exec('raise '+E)

def give(x):
    return x

def raiseE(e):
    raise e

def delvar(x):
    del x

var = {"YES": True, "NO": False, "QUOTES": "'\"", "LETTERS_UPPER": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "LETTERS_LOWER": "abcdefghijklmnopqrstuvwxyz", "LETTERS": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"}
meth = {"print": print,
        "echo": echo,
        "func": newfunc,
        "import": get_module,
        "raise": raiseE,
        "return": give,
        "python": eval,
        "quit": exit,
        "raise": raiseE,
        "del": delvar}

class compiler:
    @classmethod
    def compilelns(cls, ui):
        i = 0
        codelns = ui.splitlines()
        #while i < len(codelns):
         #   pass
    
    @classmethod
    def compileargs(cls, args):
        args = args.split("**")
        for i, arg in enumerate(args):
            if i%2 == 1:
                args[i] = cls.compilecode(arg)
        args = " ".join(args)
        args = args.split("--")
        for i, arg in enumerate(args):
            arg = arg.split(" ")
            if i > 0:
                arg[0] = str(str(var[arg[0]]))
            args[i] = " ".join(arg)
        for i, arg in enumerate(args):
            if arg == "is=":
                args[i] = "=="
            elif arg == "isnt=":
                args[i] = "not =="
        args = " ".join(args)
        args = args.split(",")
        for i, arg in enumerate(args):
            if arg == "":
                del args[i]
                continue
            part = ""
            if i < len(args)-1 and args[-1][-1] != "//":
                part = arg+","
            else:
                continue
            args[i] = part
        args = "".join(args)
        return args
    
    @classmethod
    def compilecode(cls, ui):
        if ui.endswith("/"):
            return
        ui = ui.split(" ")
        cmd = ui.pop(0)
        args = " ".join(ui)
        if len(ui) > 0:
            if ui[0] == "set=":
                del ui[0]
                var[cmd] = cls.compilecode("return "+" ".join(ui))
                return
        if cmd.startswith("_") and len(cmd.split(".")) > 1:
            cmd = cmd.split(".")
            args = cmd.pop(0)[1:]+", "+args
            cmd = ".".join(cmd)
            
        if cmd == "if":
            cmd = "testcond"
            assert(args[-1] == "{")
            args = args[:-1]
        if cmd == "func":
            assert(args[-1] == "{")
            args = args[:-1]
            args = replace(args, "(", ",")
            args = replace(args, ")", "")
            args = args.split(" ")
            args[0] = '"'+args[0]+'"'
            args = " ".join(args)
        if cmd == "class":
            assert(args[-1] == "{")
            args = args[:-1]
            args = replace(args, "(", ",")
            args = replace(args, ")", "")
            args.split(" ")
            args[0] = '"{}"'.format(args[0])
            " ".join(args)
        if args != "":
            args = cls.compileargs(args)
        output = ""
        try:
            output = runfunc(cmd, args)
        except:
            if (len(args) == 0):
                output = eval("meth[cmd]()")
            else:
                output = eval("meth[cmd]("+args+")")
        return output

    @classmethod
    def start(cls):
        while True:
            ui = input("# ")
            cls.compilecode(ui)

compiler.start()
