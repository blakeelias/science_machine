def formatting(a):
    """
    Mutates string to fit bert formatting requirements
    """
    flag=False
    for i in range(len(a)):
        if a[i]==".":
            if not Flag:
                a[i]="\t"
            else:
                a[i]="\n"
    if a[len(i)-1]=="\n":
        a[len(i)-1]=""
#repo:https://github.com/codertimo/BERT-pytorch
