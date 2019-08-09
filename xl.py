import xlrd
import xlutils
import os
def fun1(path):
    for r in os.scandir(path):
        if r.is_file():
            if not (r.name[0] == "." or r.name[0] == "~"):
                yield os.path.join(path,r.name)
            
        else:
            # when r is dir,recursive fun1(npath) returns a generator
            # it won't be called until used in a for loop.
            npath = os.path.join(path,r.name)
            for y in fun1(npath):
                # yield so it can be called by uppper fun1()
                yield os.path.join(npath,y)
                # print(os.path.join(npath,y))


path = "e:/test1/2019.7/"

filename1 = "SUM - 2019.xlsx"
data1 = xlrd.open_workbook(filename1)


full_li = []
for i in range(1,5):
    cur_table = data1.sheets(i)
    full_li.append(cur_table.col_values(3))


data2 = xlutils.copy(data1)
cplist = []
for i in range(1,5):
    cplist.append(data2.get_sheet(i))

def readfile(filename):
    data = xlrd.open_workbook(filename)
    table1 = data.sheets()[0]
    nrow = table1.nrows-3
    ncol = table1.ncols-2
    key = table1.cell_value(3,1)
    value = table1.cell_value(nrow,ncol)
    return key,value
    
for filename in fun1(path):
    key,value = readfile(filename)
    for each_li in full_li:
        if key in each_li:
            cur_ind = full_li.index(each_li)
            cur_index = each_li.index(key)
            cplist[cur_ind].write(cur_index,13,value)
data2.save(filename1)
