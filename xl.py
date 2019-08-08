import xlrd
import xlutils
filename1 = "SUM2019.xlsx"
data1 = xlrd.open_workbook(filename1)
data2 = xlutils.copy(data1)

full_li = []
for i in range(1,5):
    cur_table = data1.sheets(i)
    full_li.append(cur_table.col_values(3))
cplist = []
for i in range(1,5):
    cplist.append(data2.get_sheet(i))


filenamelist = ["A021802470-2 英国精酿 过滤槽  2000-1265 AD1.xlsx",]
for filename in filenamelist:
    data = xlrd.open_workbook(filename)
    table1 = data.sheets()[0]
    nrow = table1.nrows-3
    ncol = table1.ncols-2
    key = table1.cell_value(3,1)
    value = table1.cell_value(nrow,ncol)
    for each_li in full_li:
        if key in each_li:
            cur_ind = full_li.index(each_li)
            cur_index = each_li.index(key)
            cplist[cur_ind].write(cur_index,8,value)
data2.save(filename1)