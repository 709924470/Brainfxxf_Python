from time import sleep
def parse(instr,_units = None,_now = None,ret = None, _output = None):
    brc = []
    units = _units if _units is not None else [0]
    now = _now if _now is not None else 0
    pos = 0
    output = "" if not _output else _output
    l = 0
    for i in instr:
        if not i in "+-.,<>[]":
            continue
        if i == "+":
            units[now] += 1
        elif i == "-":
            units[now] -= 1
        elif i == ".":
            output += chr(units[now])
        elif i == ",":
            recv = ''
            while len(recv) != 1:
                recv = input("Input a character:")
            units[now] = ord(recv)
        elif i == ">":
            now += 1
            while now > len(units) - 1:
                units.append(0)
        elif i == "<":
            now = now - 1 if now >= 0 else 0
        elif i == "[":
            brc.append(pos)
        elif i == "]":
            while units[now] > 0:
                units = parse(instr[brc[-1] : pos],units,now,True,output)
            brc = brc[:-1]
        pos += 1
        l1 = pUnits(units,now,output,l)
        l = l1 if l1 > l else l 
        sleep(0.05)
    if ret:
        return units
    else:
        print(" " * l, end = '\r')
        op = [str(i)+":"+chr(i) for i in units]
        op[now] = "> " + op[now] + " <"
        op = " | ".join(op)
        print(repr(op))
        print(output)

def pUnits(units,now,out,l):
    op = [str(i)+":"+chr(i) for i in units]
    op[now] = "> " + op[now] + " <"
    op = " | ".join(op) + "  Output: " + out
    print(" " * l, end = '\r')
    print(repr(op), end="\r")
    return len(repr(op))

#parse(">>>>++++++++++++++++[<<<<++++>++++++>++++++>++++++>-]<<<<++++++.>>>>>++++[<<<<+++++>>>>-]<<<<+.>+++.>+++++++++++.")
parse(""">>>>>>>++++++++++++++++>>++++[-<++++++++>]<<[<<<<<<++++>++++++>++++++>++++++>++++++>+++++++>-]<<<<<<++++++++.>+++++.>++++++++++++..>+++++++++++++++.>>>>.<<<---------.<.>>++.<<<.<-.>>>>>>+.""")