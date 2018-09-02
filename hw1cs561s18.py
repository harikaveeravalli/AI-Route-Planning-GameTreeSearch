
from copy import deepcopy
import sys

with open(sys.argv[2],"r") as ip:
    input_data = ip.read().splitlines()
DAY = input_data[0]
NEXTPLAYER = input_data[1]
profitlist = input_data[2].strip('\n')
values = profitlist.replace('(', '').replace(')', '').split(',')
#print(len(values))
z = 1
while z <= (len(values) - 1):
    checkfloat = float(values[z])
    try:
        values[z] = int(values[z])
    except ValueError:
        values[z] = float(values[z])
    z = z + 2

RPL = dict(zip(values[::2], values[1::2]))
# RPL=(sorted(RPL.items()))

matrixdict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
              'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
              'Y': 24, 'Z': 25,
              'AA': 26, 'BB': 27, 'CC': 28, 'DD': 29, 'EE': 30, 'FF': 31, 'GG': 32, 'HH': 33, 'II': 34, 'JJ': 35,
              'KK': 36, 'LL': 37, 'MM': 38, 'NN': 39, 'OO': 40, 'PP': 41, 'QQ': 42, 'RR': 43, 'SS': 44, 'TT': 45,
              'UU': 46, 'VV': 47, 'WW': 48, 'XX': 49, 'YY': 50, 'ZZ': 51, 'AAA': 52,
              'BBB': 53, 'CCC': 54, 'DDD': 55, 'EEE': 56, 'FFF': 57, 'GGG': 58, 'HHH': 59, 'III': 60, 'JJJ': 61,
              'KKK': 62, 'LLL': 63, 'MMM': 64, 'NNN': 65, 'OOO': 66, 'PPP': 67, 'QQQ': 68, 'RRR': 69, 'SSS': 70,
              'TTT': 71, 'UUU': 72, 'VVV': 73, 'WWW': 74, 'XXX': 75, 'YYY': 76, 'ZZZ': 77}
# print(matrixdict)
#sorted_d = OrderedDict(sorted(matrixdict.items(), key=lambda x: x[1]))
#print(sorted_d)
#print(RPL)
i = 3
j = 0
#print("recursion limit")
#print(sys.getrecursionlimit())
# ADJACENY MATRIX
ADJMATRIX = []
EXPLORED_LIST = []
while i < (len(RPL) + 3):
    ADJMATRIX.append((input_data[i].strip('[').strip(']').split(',')))
    i += 1
    j += 1
EXPLORED_LIST = input_data[3 + len(RPL)].split(',')
#print(EXPLORED_LIST)
D = input_data[4 + len(RPL)]
global originaldepth
MAX_DEPTH = int(D)
originaldepth = MAX_DEPTH
#print(MAX_DEPTH)
summation = sum(RPL.values())
if DAY == 'Yesterday':
    for key, value in RPL.iteritems():
        #print(type(value))
        temp = ((summation / len(RPL)) + value) / 2
        #print(temp)
        RPL[key] = int(temp)
    #print(RPL)
R1MOVES = []
R2MOVES = []
playerlist = []
#print("explored list")
#print(EXPLORED_LIST)
#print(NEXTPLAYER)

if EXPLORED_LIST[0] == '*' and NEXTPLAYER == 'R1':
    #print("entered the * with R1")
    playerlist.append('R1')
    playerlist.append('R2')
if EXPLORED_LIST[0] == '*' and NEXTPLAYER == 'R2':
    playerlist.append('R2')
    playerlist.append('R1')
if len(EXPLORED_LIST) == 1 and NEXTPLAYER == 'R1':
    #print("entered the if statement")
    if EXPLORED_LIST[0] != '*':
        #print("entered for R1 *")
        playerlist.append('R2')
        playerlist.append('R1')
        R2MOVES.append(EXPLORED_LIST[0])
if len(EXPLORED_LIST) == 1 and NEXTPLAYER == 'R2':
    #print("entered R2 if statement")
    if EXPLORED_LIST[0] != '*':
        playerlist.append('R1')
        playerlist.append('R2')
        R1MOVES.append(EXPLORED_LIST[0])
if len(EXPLORED_LIST) > 1 and NEXTPLAYER == 'R1':
    if len(EXPLORED_LIST) % 2 == 0:
        playerlist.append('R1')
        playerlist.append('R2')
        for i in range(len(EXPLORED_LIST)):
            if i % 2 == 0:
                R1MOVES.append(EXPLORED_LIST[i])
            else:
                R2MOVES.append(EXPLORED_LIST[i])
    else:
        playerlist.append('R2')
        playerlist.append('R1')
        for i in range(len(EXPLORED_LIST)):
            if i % 2 == 0:
                R2MOVES.append(EXPLORED_LIST[i])
            else:
                R1MOVES.append(EXPLORED_LIST[i])
if len(EXPLORED_LIST) > 1 and NEXTPLAYER == 'R2':
    if len(EXPLORED_LIST) % 2 == 0:
        playerlist.append('R2')
        playerlist.append('R1')
        for i in range(len(EXPLORED_LIST)):
            if i % 2 == 0:
                R2MOVES.append(EXPLORED_LIST[i])
            else:
                R1MOVES.append(EXPLORED_LIST[i])
    else:
        playerlist.append('R1')
        playerlist.append('R2')
        for i in range(len(EXPLORED_LIST)):
            if i % 2 == 0:
                R1MOVES.append(EXPLORED_LIST[i])
            else:
                R2MOVES.append(EXPLORED_LIST[i])
#print(R1MOVES)
#print(R2MOVES)
#print(":player list")
#print(playerlist)


class Buildalgo:
    def __init__(self, NEXTPLAYER, RPL, ADJMATRIX, EXPLORED_LIST, MAX_DEPTH, R1MOVES, R2MOVES):
        self.NEXTPLAYER = NEXTPLAYER
        self.ADJMATRIX = ADJMATRIX
        self.EXPLORED_LIST = EXPLORED_LIST
        self.MAX_DEPTH = MAX_DEPTH
        self.RPL = RPL
        self.R1MOVES = R1MOVES
        self.R2MOVES = R2MOVES
        self.POSSIBLEMOVES1 = []
        self.POSSIBLEMOVES2 = []
        self.MEMBERPARENT = ''
        self.utilityVal = 0
        self.NEXT_MOVE = ''
        self.CURRENTNODE=''
    def possiblemoves(self, player, R1MOVES, R2MOVES):
        self.R1MOVES = R1MOVES
        self.R2MOVES = R2MOVES

        if player == 'R2' and len(self.R2MOVES) > 0:
            index2 = 0
            possiblenode = ''
            i = 0
            examplelist = []
            trylist = []
            # print("R2MOVES")
            # print(self.R2MOVES)
            # for i in range(len(self.R2MOVES)):
            while i < len(self.R2MOVES):
                matrixrow = ord(self.R2MOVES[i])-65
                # print(matrixrow)
                for index2 in range(len(self.RPL)):
                    if self.ADJMATRIX[matrixrow][index2] == '1':
                        #possiblenode = list(sorted_d.keys())[list(sorted_d.values()).index(index2)]
                        # print(possiblenode)
                        possiblenode=chr(index2+65)
                        if possiblenode not in self.R2MOVES and possiblenode not in self.R1MOVES:
                            # print("entered to append")
                            examplelist.append(possiblenode)
                i = i + 1

            for num in examplelist:
                if num not in trylist:
                    trylist.append(num)

            trylist.sort()
            trylist.sort(key=len)

            self.POSSIBLEMOVES2 = deepcopy(trylist)
            #print("entered R2 possible moves")
            #print(self.POSSIBLEMOVES2)
            return self.POSSIBLEMOVES2
        if player == 'R2' and self.R2MOVES == []:
            list2 = sorted(self.RPL.keys())
            for index in range(len(list2)):
                if list2[index] not in self.R1MOVES and list2[index] not in self.R2MOVES:
                    self.POSSIBLEMOVES2.append(list2[index])
            return self.POSSIBLEMOVES2
        if player == 'R1' and self.R1MOVES == []:
            list2 = sorted(self.RPL.keys())
            for index in range(len(list2)):
                if list2[index] not in self.R1MOVES and list2[index] not in self.R2MOVES:
                    self.POSSIBLEMOVES1.append(list2[index])
            return self.POSSIBLEMOVES1
            # r2 is the next player and has taken moves peviously

        if player == 'R1' and len(self.R1MOVES) > 0:
            examplelist1 = []
            trylist = []
            i = 0
            index1 = 0
            # print("R1MOVES")
            # print(self.R1MOVES)
            while i < len(self.R1MOVES):

                matrixrow = ord(self.R1MOVES[i])-65
                # print(matrixrow)
                for index1 in range(len(self.RPL)):
                    if self.ADJMATRIX[matrixrow][index1] == '1':
                        #possiblenode = list(sorted_d.keys())[list(sorted_d.values()).index(index1)]
                        possiblenode=chr(index1+65)
                        if possiblenode not in self.R1MOVES and possiblenode not in self.R2MOVES:
                            # print("entered to append")
                            examplelist1.append(possiblenode)

                i = i + 1
            for num in examplelist1:
                if num not in trylist:
                    trylist.append(num)

            trylist.sort()
            trylist.sort(key=len)

            # list(set(examplelist)).sort(key=lambda item:(len(item),item))
            self.POSSIBLEMOVES1 = deepcopy(trylist)
            #print("entered R1 possible nodes")
            #print(self.POSSIBLEMOVES1)
            return self.POSSIBLEMOVES1

    def make_move(self, ib, obj, player):
        if player == 'R1':
            self.NEXT_MOVE = obj.POSSIBLEMOVES1[ib]
            if obj.R1MOVES!=[] :
                self.MEMBERPARENT=obj.R1MOVES[-1]
            else:
                self.MEMBERPARENT=obj.POSSIBLEMOVES1[ib]
            self.CURRENTNODE=obj.POSSIBLEMOVES1[ib]
            self.R1MOVES.append(obj.POSSIBLEMOVES1[ib])
            #print("R1MOVES")
            #print(self.R1MOVES)
            #print("parent")
            #print(self.MEMBERPARENT)

        elif player == 'R2':
            self.NEXT_MOVE = obj.POSSIBLEMOVES2[ib]
            if obj.R2MOVES!=[]:
                self.MEMBERPARENT = obj.R2MOVES[-1]
            else:
                self.MEMBERPARENT=obj.POSSIBLEMOVES2[ib]
            self.CURRENTNODE=obj.POSSIBLEMOVES2[ib]
            self.R2MOVES.append(obj.POSSIBLEMOVES2[ib])
            #print("R2MOVES")
            #print(self.R2MOVES)
            #print("parent")
            #print(self.MEMBERPARENT)
            # self.NEXT_MOVE=obj.POSSIBLEMOVES2[i]
        # print(self.NEXT_MOVE)

        getutilityvalue(self, player)
        return self


def getutilityvalue(objname, player):
    R1utilityval = 0
    R2utilityval = 0
    if (player == 'R1'):
        for i in range(len(objname.R1MOVES)):
            R1utilityval += RPL[objname.R1MOVES[i]]
        objname.utilityVal = R1utilityval
        # print(objname.utilityVal)
    else:
        for i in range(len(objname.R2MOVES)):
            R2utilityval += RPL[objname.R2MOVES[i]]
        objname.utilityVal = R2utilityval
        # print(objname.utilityVal)
    return objname.utilityVal


passflag = [False, False]
terminalflag = False
global valuearray
valuearray = []
valuex=['',0]
global nodesarray
nodesarray=[]



def minimax(player, maxdepth, R1MOVES, R2MOVES, obj):
    #print("inside minimax")
    #print("depth", maxdepth)
    #print("valuex")
    #print(valuex)

    global passflag
    global best_move
    global parent
    best_move=''
    m = 0
    n = 0
    q = 0
    r = 0
    value1=[]
    # if maxdepth == originaldepth:
    #   valuearray.append(obj.utilityVal)
    #  return obj.utilityVal
    # obj.possiblemoves(playerlist[0], obj.R1MOVES, obj.R2MOVES)
    arrytopass2=[]
    # getutilityvalue(obj, player)
    if passflag[0] == True and passflag[1] == True:
        #print("enterd passflag condition")
        valuearray.append(obj.utilityVal)
        #nodesarray.append(obj.MEMBERPARENT)
        # print(obj.utilityVal)

        arrytopass2.append(obj.MEMBERPARENT)
        arrytopass2.append(obj.utilityVal)
        return arrytopass2
    maxval=[]
    maxval=['',0]


    if player == playerlist[0]:
        arrytopass1=[]
        if maxdepth == originaldepth:
            #print("entered player of 0 maxdepth")
            #print("print node and value inside maxdepth reached")
            #print(obj.MEMBERPARENT, obj.utilityVal)
            #print ("R1 moves at maxdepth")
            #print (obj.R1MOVES)
            #print ("R2 moves at maxdepth")
            #print (obj.R2MOVES)

            valuearray.append(obj.utilityVal)
            nodesarray.append(obj.MEMBERPARENT)
            # print(obj.utilityVal)

            arrytopass1.append(obj.MEMBERPARENT)
            arrytopass1.append(obj.utilityVal)
            return arrytopass1
           # return obj.utilityVal
        obj.possiblemoves(playerlist[0], obj.R1MOVES, obj.R2MOVES)
        # getutilityvalue(obj, player)
        valuex[0]=''
        valuex[1] = -float('inf')
        #print("entered the block")
        #	#entered the max function

        if player == 'R1':
            objlist = [j for j in range(len(obj.POSSIBLEMOVES1))]
        else:
            objlist = [j for j in range(len(obj.POSSIBLEMOVES2))]
        #print("possiblemoves R1")
        #print(obj.POSSIBLEMOVES1)
        if player == 'R1' and obj.POSSIBLEMOVES1 == []:
            formchild1 = deepcopy(obj.R1MOVES)
            formchild2 = deepcopy(obj.R2MOVES)


            algobj = Buildalgo(playerlist[0], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH, formchild1,
                               formchild2)
            algobj.utilityVal = getutilityvalue(algobj, player)
            #algobj.NEXT_MOVE = 'pass'
            algobj.CURRENTNODE='pass'
            if  maxdepth == (val + 1) and len(formchild2) > 0:
                algobj.MEMBERPARENT= formchild2[-1]
                parent = deepcopy(algobj.MEMBERPARENT)
                #print("parent")
                #print(algobj.MEMBERPARENT)
            if maxdepth > val+1:
                #print("parent value outside")
                #print(parent)
                algobj.MEMBERPARENT=parent
            passflag[0] = True

            #if len(formchild1) > 0:
             #   algobj.MEMBERPARENT = formchild1[-1]
            value1 = minimax(playerlist[1], maxdepth + 1, algobj.R1MOVES, algobj.R2MOVES, algobj)
            #print(value1[1])
            if value1[1] > valuex[1]:
                valuex[1] = value1[1]
                valuex[0]= parent
                if maxdepth == originaldepth:
                    best_move = parent
                #print("NODE")
                #print(valuex[0])


        if player == 'R1' and len(obj.POSSIBLEMOVES1) > 0:
            for m in range(len(obj.POSSIBLEMOVES1)):
                formchild1 = deepcopy(obj.R1MOVES)
                formchild2 = deepcopy(obj.R2MOVES)

                objlist[m] = Buildalgo(playerlist[0], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH,
                                       formchild1, formchild2)
                objlist[m] = objlist[m].make_move(m, obj, player)
                # maxdepth=maxdepth-1
                #print(objlist[m].NEXT_MOVE)
                if  maxdepth == (val + 1) and len(formchild2)>0:
                    objlist[m].MEMBERPARENT=formchild2[-1]
                    parent = deepcopy(objlist[m].MEMBERPARENT)
                    #print("parent")
                    #print(objlist[m].MEMBERPARENT)
                if maxdepth > val + 1:
                    #print("parent value outside")
                    #print (parent)
                    objlist[m].MEMBERPARENT=parent
                value1 = minimax(playerlist[1], maxdepth + 1, objlist[m].R1MOVES, objlist[m].R2MOVES, objlist[m])
                value1[0]=parent
                #print(value1[1])
                if value1[1] > valuex[1]:
                    valuex[1] = value1[1]
                    valuex[0] = value1[0]

                    if maxdepth == originaldepth:
                        best_move=parent
                    #print("NODE")
                    #print(valuex[0])

        passflag[0] = False
        # print("objlist1",objlist)
        if player == 'R2' and obj.POSSIBLEMOVES2 == []:
            formchild1 = deepcopy(obj.R1MOVES)
            formchild2 = deepcopy(obj.R2MOVES)
            #print ("formchild2 R2 moves")
            #print (formchild2)
            algobj = Buildalgo(playerlist[0], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH, formchild1,
                               formchild2)
            algobj.utilityVal = getutilityvalue(algobj, player)
            algobj.NEXT_MOVE = 'pass'
            algobj.CURRENTNODE='pass'
            passflag[0] = True
            if  maxdepth == (val + 1) and len(formchild1)>0 :
                algobj.MEMBERPARENT=formchild1[-1]
                parent = deepcopy(algobj.MEMBERPARENT)
                #print ("parent")
                #print (algobj.MEMBERPARENT)
            if maxdepth > val+1:
                #print ("parent value outside")
                #print (parent)
                algobj.MEMBERPARENT=parent
            #trylength=len(formchild1)
            #if trylength>0:
            #    algobj.MEMBERPARENT=formchild1[-1]



            # maxdepth=maxdepth-1
            value1 = minimax(playerlist[1], maxdepth + 1, algobj.R1MOVES, algobj.R2MOVES, algobj)
            #print(value1[1])
            if value1[1] > valuex[1]:
                valuex[1] = value1[1]

                valuex[0] = parent
                if maxdepth == originaldepth:
                    best_move = parent

                #print("NODE")
                #print(valuex[0])

        if player == 'R2' and len(obj.POSSIBLEMOVES2) > 0:
            for n in range(len(obj.POSSIBLEMOVES2)):
                formchild1 = deepcopy(obj.R1MOVES)
                formchild2 = deepcopy(obj.R2MOVES)
                #print ("R2MOVES PREVIOUS MOVES player0")
                #print (formchild2)
                objlist[n] = Buildalgo(playerlist[0], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH,
                                       formchild1, formchild2)
                objlist[n] = objlist[n].make_move(n, obj, player)
                # maxdepth=maxdepth-1
                #objlist[n].memberparent=formchild2[len(formchild2)-1]
                #print(objlist[n].memberparent)
                if  maxdepth == (val + 1) and len(formchild1)>0:
                    objlist[n].MEMBERPARENT= formchild1[-1]
                    parent = deepcopy(objlist[n].MEMBERPARENT)
                    #print ("parent")
                    #print (objlist[n].MEMBERPARENT)
                if maxdepth > val + 1:
                    #print ("parent value outside")
                    #print (parent)
                    objlist[n].MEMBERPARENT=parent
                value1 = minimax(playerlist[1], maxdepth + 1, objlist[n].R1MOVES, objlist[n].R2MOVES, objlist[n])

                #print(value1[1])
                if value1[1] > valuex[1]:
                    valuex[1] = value1[1]
                    valuex[0] = parent
                    if maxdepth == originaldepth:
                        best_move=parent
                    #print("NODE")
                    #print(valuex[0])
        passflag[0] = False
        return valuex
        # objlist=[j for j in range(len(obj.POSSIBLEMOVES2))]
    if player == playerlist[1]:
        # print("entered block for player[1]")
        arrytopass=[]
        if maxdepth == originaldepth:
            #print("entered player maxdepth")
            #print("print node and value 1 maxdepth reached")
            #print(obj.MEMBERPARENT, obj.utilityVal)
            nodesarray.append(obj.MEMBERPARENT)
            valuearray.append(obj.utilityVal)
            arrytopass.append(obj.MEMBERPARENT)
            arrytopass.append(obj.utilityVal)
            return arrytopass
        obj.possiblemoves(playerlist[1], obj.R1MOVES, obj.R2MOVES)
        valuex[0]=''
        valuex[1] = float('inf')

        if player == 'R1':
            objlist = [j for j in range(len(obj.POSSIBLEMOVES1))]
        else:
            objlist = [j for j in range(len(obj.POSSIBLEMOVES2))]

        if player == 'R1' and obj.POSSIBLEMOVES1 == []:
            formchild1 = deepcopy(obj.R1MOVES)
            formchild2 = deepcopy(obj.R2MOVES)

            algobj = Buildalgo(playerlist[1], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH, formchild1,
                               formchild2)
            algobj.utilityVal = getutilityvalue(algobj, player)
            algobj.NEXT_MOVE = 'pass'
            algobj.CURRENTNODE='pass'

            passflag[1] = True
            if len(formchild2) > 0 and maxdepth == (val + 1):
                algobj.MEMBERPARENT = formchild2[-1]
                parent = deepcopy(algobj.MEMBERPARENT)
                #print ("parent")
                #print (algobj.MEMBERPARENT)
            if maxdepth > val+1:
                #print ("parent value outside")
                #print (parent)
                algobj.MEMBERPARENT=parent
            value1 = minimax(playerlist[0], maxdepth + 1, algobj.R1MOVES, algobj.R2MOVES, algobj)
            #print(value1[1])
            if value1[1] < valuex[1]:
                valuex[1] = value1[1]
                valuex[0] = parent
                if maxdepth == originaldepth:
                    best_move = parent
                #print("NODE")
                #print(valuex[0])

        if player == 'R1' and len(obj.POSSIBLEMOVES1) > 0:
            for q in range(len(obj.POSSIBLEMOVES1)):
                formchild1 = deepcopy(obj.R1MOVES)
                formchild2 = deepcopy(obj.R2MOVES)

                objlist[q] = Buildalgo(playerlist[1], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH,
                                       formchild1, formchild2)
                objlist[q] = objlist[q].make_move(q, obj, player)
                if len(formchild2)>0 and maxdepth == (val + 1):
                    objlist[q].MEMBERPARENT=formchild2[-1]
                    parent = deepcopy(objlist[q].MEMBERPARENT)
                    #print ("parent")
                    #print (objlist[q].MEMBERPARENT)
                if maxdepth > val + 1:
                    #print ("parent value outside")
                    #print (parent)
                    objlist[q].MEMBERPARENT=parent
                # maxdepth=maxdepth-1
                #objlist[q].memberparent = formchild1[len(formchild1) - 1]
                #print(objlist[q].NEXT_MOVE)
                value1 = minimax(playerlist[0], maxdepth + 1, objlist[q].R1MOVES, objlist[q].R2MOVES, objlist[q])
                #print(value1[1])
                if value1 < valuex:
                    valuex[1] = value1[1]
                    valuex[1] = parent
                    if maxdepth == originaldepth:
                        best_move=parent
                    #print("NODE")
                    #print(valuex[0])

        passflag[1] = False

        if player == 'R2' and obj.POSSIBLEMOVES2 == []:
            formchild1 = deepcopy(obj.R1MOVES)
            formchild2 = deepcopy(obj.R2MOVES)

            algobj = Buildalgo(playerlist[1], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH, formchild1,
                               formchild2)
            algobj.utilityVal = getutilityvalue(algobj, player)
            algobj.NEXT_MOVE = 'pass'
            passflag[1] = True
            if len(formchild1)>0 and maxdepth == (val + 1):
                algobj.MEMBERPARENT=formchild1[-1]
                parent = deepcopy(algobj.MEMBERPARENT)
                #print ("parent")
                #print (algobj.MEMBERPARENT)

            if maxdepth > val+1:
                #print ("parent value outside")
                #print (parent)

                algobj.MEMBERPARENT=parent
            value1 = minimax(playerlist[0], maxdepth + 1, algobj.R1MOVES, algobj.R2MOVES, algobj)
            #print(value1[1])
            if value1[1] < valuex[1]:
                valuex[1] = value1[1]
                valuex[1] = parent
                if maxdepth == originaldepth:
                    best_move = parent
                #print("NODE")
                #print(valuex[0])



        if player == 'R2' and len(obj.POSSIBLEMOVES2) > 0:
            for r in range(len(obj.POSSIBLEMOVES2)):
                formchild1 = deepcopy(obj.R1MOVES)
                formchild2 = deepcopy(obj.R2MOVES)

                objlist[r] = Buildalgo(playerlist[1], obj.RPL, obj.ADJMATRIX, obj.EXPLORED_LIST, obj.MAX_DEPTH,
                                       formchild1, formchild2)
                objlist[r] = objlist[r].make_move(r, obj, player)
                if len(formchild1)>0 and maxdepth == (val + 1) :
                    objlist[r].MEMBERPARENT=formchild1[-1]
                    parent = deepcopy(objlist[r].MEMBERPARENT)
                    #print("parent")
                    #print (objlist[r].MEMBERPARENT)
                if maxdepth > val + 1:
                    #print("parent value outside")
                    #print(parent)
                    objlist[r].MEMBERPARENT=parent
                value1 = minimax(playerlist[0], maxdepth + 1, objlist[r].R1MOVES, objlist[r].R2MOVES, objlist[r])
                #print(value1[1])
                if value1[1] < valuex[1]:
                    valuex[1] = value1[1]
                    valuex[0] = parent
                    if maxdepth == originaldepth:
                        best_move=parent
                    #print("NODE")
                    #print(valuex[0])


        passflag[1] = False

        return valuex


parentobj = Buildalgo(NEXTPLAYER, RPL, ADJMATRIX, EXPLORED_LIST, MAX_DEPTH, R1MOVES, R2MOVES)
#print(parentobj.R2MOVES)
#print(parentobj.R1MOVES)
#print("NEXT PLAYER")
#print(NEXTPLAYER)

global val

outputfile=open('output.txt',"w+")
tmp = []
if originaldepth == 0:
    if NEXTPLAYER == 'R1':
        parentobj.possiblemoves(NEXTPLAYER, R1MOVES, R2MOVES)
        for i in range(len(parentobj.POSSIBLEMOVES1)):
            tmp.append((RPL[parentobj.POSSIBLEMOVES1[i]]))
        nextval = max(RPL.items(), key=operator.itemgetter(1))[0]
        #print(nextval)
        outputfile.write(nextval+"\n")
        tmp1 = [str(a) for a in tmp]
        outputfile.write(','.join(tmp1))
    elif NEXTPLAYER == 'R2':
        parentobj.possiblemoves(NEXTPLAYER, R1MOVES, R2MOVES)
        for i in range(len(parentobj.POSSIBLEMOVES2)):
            tmp.append((RPL[parentobj.POSSIBLEMOVES2[i]]))
        nextval = max(RPL.items(), key=operator.itemgetter(1))[0]
        #print(nextval)
        outputfile.write(nextval+"\n")
        tmp1 = [str(a) for a in tmp]
        #print(','.join(tmp1))
        outputfile.write(','.join(tmp1))

else:

    if EXPLORED_LIST[0] == '*':
        val = -1
    else:
        val = len(EXPLORED_LIST) - 1

    x = minimax(NEXTPLAYER, val, R1MOVES, R2MOVES, parentobj)

    #print (x)
#print("value array")
#print(best_move)
maxpos=valuearray.index(max(valuearray))
outputfile.write(nodesarray[maxpos]+'\n')
#print(valuearray)
tmp1=[str(a) for a in valuearray]
outputfile.write(','.join(tmp1))



