import xlrd
import xlwt
import re
file=xlrd.open_workbook('接口验证规范表-20200507.xlsx')
data_ori=file.sheet_by_name('Sheet1')

nrows=data_ori.nrows
ncols=data_ori.ncols
'''
dt=入参报文
{
    "params": {
        "userMobile": "13709080969"
    }
}
{
    "params": {
        "userMobile": "15281639037"
    }
}
dt=dt.strip().replace('\n','')
print(re.match(r'入参报文(.*?)$',dt).group(1))

'''
for i in range (nrows):
	try:
		url=data_ori.cell(i,0).value
	except:
		pass
	else:
		url1=str(url.split('\n')[0])
		print(url1)
		url_new=re.match(r'post (.*?)$',url1)
		print('+'*30,url_new)
	

	#head=data_ori.cell(i,1).value
	#data=data_ori.cell(i,3).value
	


cell_A1=data.cell(4,0).value#直接取单元格值
