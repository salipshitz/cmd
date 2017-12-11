from os import system

var = {"YES": True, "NO": False}

class compiler:
    @classmethod
    def compileargs(cls, args):
        args = args.split(",")
        for i, arg in enumerate(args):
            if arg == "":
                del args[i]
                continue
            part = ""
            if i < len(args)-1 and args[-1][-1] != "//":
                part = arg+","
            elif args[-1][-1] != "\\":
                part = args.pop(-1)+","
            else:
                continue
            args[i] = part
            args = "".join(args)
    
    @classmethod
    def compilecode(cls, ui):
        ui = ui.split(" ")
        cmd = ui.pop(0)
        args = " ".join(ui)
        if cmd == "if":
            cmd = "testcond"
            assert(args[-1] = "}")
            del args[-1]
        if cmd == "func":
            assert(args[-1] = "}")
            del args[-1]
            args = "".join("".join(args.split("(").split(")")))
        if args != "":
            args = cls.compileargs(args)
        exec(cmd+"("+args+")")
    
    @classmethod
    def start(cls, args):
        while True:
            ui = input("# ")
            cls.compilecode(ui)

def runfunc(nm, *args):
    for line in var[nm].splitlines():
        compiler.compilecode()

def func(nm, *args):
    code = ""
    while True:
        code += "\n"+input("")
        if code.endswith("}"):
            del code[-1]
            break
    var[nm] = {"args": *args, "code": code}

def end():
    exit()

def clear():
    system('cls')

compiler.start()
