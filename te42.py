# _*- coding: utf-8 -*-
from sys import exit
from random import randint


class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print("\n--------")
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)

    def central_corridor(self):
        # 打印字符串
        print("The Gothons of Planet Percal #25 have invaded your ship and destroy")
        print("you entire crew.  You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print(
            "a Gothon jumps put, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        # 通过input("> ")命令输入值，并将值赋予action变量
        print "You can use these methods.'shoot!', 'dodge!', 'tell a joke'"
        action = input("> ")

        # 通过if语句判断action变量的值是否等于shoot!字符串
        # 如果if语句判断为True，就把缩进print语句执行，并返回death字符串(忽略剩下的elif和else)
        # 如果if语句判断为False，执行elif(或else)语句
        if action == "shoot!":
            print(
                "Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print(
                "off your aim.  Your laser hits his costume but misses him entirely.  This")
            print("completely ruins his brand new costume his mother bought him, which")
            print(
                "makes him fly into an insane rage and blast you repeatedly in the face until")
            print("you are dead.  Then he eats you.")
            return 'death'

        # elif语句判断action变量的值是否等于dodge!字符串
        # 如果elif语句判断为True，就把缩进print语句执行，并返回death字符串(忽略剩下的elif和else)
        # 如果elif语句判断为False，执行下一个elif(或else)语句
        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you.")
            return 'death'

        # elif语句判断action变量的值是否等于tell a joke字符串
        # 如果elif语句判断为True，就把缩进print语句执行，并返回laser_weapon_armory字符串(忽略剩下的elif和else)
        # 如果elif语句判断为False，执行剩下的else语句
        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print(
                "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
            print(
                "The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'
        # 打印DOES NOT COMPUTE!字符串
        # 返回central_corridor字符串
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

    def laser_weapon_armory(self):
        # 打印字符串

        # random.randint(a, b)，用于生成一个指定范围内的整数，
        # 其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
        # 字符串包含 %d 格式化变量,变量名n均为：
        # 参数为(1, 9),生成的随机数：1 <= n <= 9
        # 将'%d%d%d'字符串赋值给code变量
        # 通过input("[keypad]> ")命令输入值，并将值赋予guess变量
        # 将0整数赋值给guesses变量
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding.  It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container.  There's a keypad lock on the box")
        print("and you need the code to get the bomb out.  If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb.  The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        print "输入3位数密码（最多只能输入10次）："
        guess = input("[keypad]> ")
        guesses = 0

        # guess变量的值不等于code变量的值
        # and运算是与运算，所有都为True，and运算结果才是True
        # while语句，只要条件满足就不断循环缩进语句，条件不满足时退出循环
        # 即：guess变量的值不等于code变量的布尔值为True，guesses变量的值小于10的布尔值为True时，不断循环
        # 它们的and运算结果(其中一个条件布尔值)为False时退出循环
        while guess != code and guesses < 10:
            # 缩进语句：
            # 打印"BZZZZEDDD!"字符串
            # +=是加法赋值运算符，比如c += a 等效于 c = c + a
            # guesses += 1 等效于 guesses = guesses + 1，
            # 即：将guesses变量的值与1整数的值相加的结果存放到guesses变量
            # 通过input("[keypad]> ")命令输入值，并将值赋予guess变量
            print("BZZZZEDDD!")
            guesses += 1
            print "输入3位数："
            guess = input("[keypad]> ")

        # 通过if语句判断guess变量的值是否等于code变量的值：
        # 如果if语句判断为True，就把缩进print语句执行，并返回'the_bridge'字符串(忽略剩下的elif和else)
        # 如果if语句判断为False，执行elif或else语句
        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast you can to the")
            print("bridge_where you must place it in the right spot.")
            return 'the_bridge'

        # 打印字符串
        # 返回 'death'字符串
        else:
            print("The lock buzzes one last time and then you hear sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'

    # 定义the_bridge()函数
    def the_bridge():
        # 打印字符串
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship.  Each of them has an even uglier")
        print("clown costume than the last.  They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        # 通过input("> ")命令输入值，并将值赋予 action 变量
        print "请输入你的决定：'throw the bomb', 'slowly place the bomb', "
        action = input("> ")

        # 通过if语句判断 action 变量的值是否等于"throw the bomb"字符串的值：
        # 如果if语句判断为True，就把缩进print语句执行，并返回'death'字符串(忽略剩下的elif和else)
        # 如果if语句判断为False，执行elif或else语句
        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door.  Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. You die knowing they will probably blow up when")
            print("it goes off.")
            return 'death'

        # elif语句判断 action 变量的值是否等于"slowly place the bomb"字符串
        # 如果elif语句判断为True，就把缩进print语句执行，并返回'escape_pod'字符串(忽略剩下的elif和else)
        # 如果elif语句判断为False，执行下一个elif(或else)语句
        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under you arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return 'escape_pod'
        # 打印字符串
        # 返回"the_bright"字符串
        else:
            print("DOES NOT COMPUTE!")
            return "the_bright"

    # 定义 escape_pod()函数
    def escape_pod():
        # 打印字符串
        # 将randint(1,5)随机数赋值给good_pod变量
        # 通过input("[pod #]> ")命令输入值，并将值赋予 guess 变量
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes.  It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference.  You get to the chamber with the escape pods, and")
        print("now need to pick one to take.  Some of them could be damaged")
        print("but you don't have time to look.  There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        # 在上一段代码中input()返回的数据类型是str，str不能直接与整数比较，
        # 必须先把str转换成整数(注：int无法转换「不是合法数字」的字符串)：
        # 通过if语句判断 int(guess) 变量的值是否不等于 good_pod 变量的值：
        # 如果if语句判断为True，就把缩进print语句执行，并返回'death'字符串(忽略剩下的elif和else)
        # 如果if语句判断为False，执行elif或else语句
        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the world of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return 'death'
        # 打印字符串
        # exit(0)：无错误退出
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below. Asit flies to the planet, you look")
            print("back and see you ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You won!")
            exit(0)


a_game = Game("central_corridor")
a_game.play()
