from os import system

class cmd:
    play = True
    
    @staticmethod
    def start():
        while True:
            while cmd.play:
                ui = input("$ ")
                ui = ui.split(" ")
                cmd = ui.pop(0)
                args = " ".join(ui)
                if args != "":
                    args = args.split(",")
                    for i in range(len(args)):
                        part = ""
                        if i < len(args) and args[i][len(args[i])-1] != "\\":
                            part = args[i]+","
                        elif args[i][len(args[i])-1] != "\\":
                            part = pop(len(args[i]))+","
                        else:
                            part = args[i]
                        args[i] = part
                    args = "".join(args)
                exec(cmd+"("+args+")")

    @staticmethod
    def resume():
        play = True

    @staticmethod
    def pause():
        play = False

def quit():
    exit()

def clear():
    system('cls')

def cmd:
    cmd.pause()

    cmd.play()

cmd.start()
