from os import system
from importlib import import_module

meth = {}

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

def func(nm, *args):
    code = ""
    while True:
        code += "\n"+input("")
        if code.endswith("}"):
            del code[-1]
            break
    var[nm] = {"args": args, "code": code}

def echo(*args, sep=' ', end='\n'):
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

var = {"YES": True, "NO": False, "QUOTES": "'\"", "LETTERS_UPPER": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "LETTERS_LOWER": "abcdefghijklmnopqrstuvwxyz", "LETTERS": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"}
meth = {"print": print, "echo": echo, "func": func, "import": get_module}

class compiler:
    @classmethod
    def compileargs(cls, args):
        args = args.split("**")
        for i, arg in enumerate(args):
            if i%2 == 1:
                args[i] = cls.compilecode(arg)
        args = " ".join(args)
        args = args.split("--")
        for i, arg in enumerate(args):
            if i%2 == 1:
                args[i] = var[arg]
        for i, arg in enumerate(args):
            if arg == "is":
                args[i] = "=="
            elif arg == "isnt":
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
            print(i, len(args))
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
        if cmd == "if":
            cmd = "testcond"
            assert(args[-1] == "{")
            args = args[:-1]
        if cmd == "func":
            assert(args[-1] == "{")
            args = args[:-1]
            print(type(args))
            args = replace(args, "(", "")
            args = replace(args, ")", "")
            args[0] = '"{}"'.format(args[0])
        if args != "":
            args = cls.compileargs(args)
        output = ""
        try:
            output = runfunc(cmd, args)
        except:
            output = meth[cmd](args)

    @classmethod
    def start(cls):
        while True:
            ui = input("# ")
            cls.compilecode(ui)

compiler.start()
