def arithmetic_arranger(problems, show_answers=False):
    n1s,os,n2s=[],[],[]
    p1,p2,p3='','',''
    for c in problems:
        nbs=c.split()
        n1s.append(nbs[0])
        os.append(nbs[1].strip())
        n2s.append(nbs[2])
    if len(problems)>5:
        return 'Error: Too many problems.'
    for o in os:
        if o!="+" and o!="-":
            return "Error: Operator must be '+' or '-'."
    for i in range(len(n1s)):
        if not n1s[i].isdigit() or not n2s[i].isdigit():
            return 'Error: Numbers must only contain digits.' 
        if len(n1s[i])>4 or len(n2s[i])>4:
            return 'Error: Numbers cannot be more than four digits.'
    
    for i in range(len(problems)):
        justi=max(len(n1s[i]),len(n2s[i]))+2
        p1+=str(n1s[i].rjust(justi))+'    ' if i!=len(problems)-1 else str(n1s[i].rjust(justi))+"\n"
    for i in range(len(problems)):
        justi=max(len(n1s[i]),len(n2s[i]))+2
        p2+=str(os[i]+n2s[i].rjust(justi-1))+'    ' if i!=len(problems)-1 else str(os[i]+n2s[i].rjust(justi-1))+"\n"
    for i in range(len(problems)):
        justi=max(len(n1s[i]),len(n2s[i]))+2
        p3+="-"*justi+'    ' if i!=len(problems)-1 else "-"*justi
    if show_answers:
        p4=''
        for i in range(len(problems)):
            justi=max(len(n1s[i]),len(n2s[i]))+2
            if os[i]=="+":
                p4+=str(int(n1s[i])+int(n2s[i])).rjust(justi)+'    ' if i!=len(problems)-1 else str(int(n1s[i])+int(n2s[i])).rjust(justi)
            else:
                p4+=str(int(n1s[i])-int(n2s[i])).rjust(justi)+'    ' if i!=len(problems)-1 else str(int(n1s[i])-int(n2s[i])).rjust(justi)
        return p1+p2+p3+"\n"+p4
    else:
        return p1+p2+p3

print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))