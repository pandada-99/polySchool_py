# 220503 딥러닝수학(신교수님)

def read_value(file_name):
   rtn_list = []
   cnt = 0
   try:
       f = open(file_name, "r") # r: read, w: write, rw
       while True:
           line = f.readline()
           #  73  80  75  152\n
           if not line: break
           # new lint(\n)을 제거하고. 탭(\t)으로 split
           # [73, 80, 75, 152, 93, 88, 93, 185,...]
           rtn_list.append(list(map(float, (line.rstrip("\n")).split("\t"))))
           cnt += 1
       f.close()
   except FileNotFoundError as e:
       print(e)

   return rtn_list, cnt


if __name__=='__main__':
    rtn_list = read_value("data/score_mlr03.txt")
    print(rtn_list)