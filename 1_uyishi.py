    
#                      -act 1- 
# s = "ffgabnnkmm"
# s = "farrabennlakot"
s = input(">>> ")
lst = []
st = ""
for i in s:
    if i not in st:
        st = st + i
    else:
        lst.append(st)
        st = i
lst.append(st)
max = max(lst, key=lambda x: len(x))
print(max)