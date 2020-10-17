import csv
import pandas as pd
import os

SaveFile_Name = "all.csv"
if __name__ == "__main__":
    rootdir = '/home/cdroad/Downloads/20201017/'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = pd.read_csv(rootdir+list[0])   #编码默认UTF-8，若乱码自行更改

    # for i in range(0, len(list)):
    #     path = os.path.join(rootdir, list[i])
    #     # if os.path.isfile(path):
    #     # # 你想对文件的操作
    #     print (path)

def jinghua1():
    n = 0
    str1 = "小区"
    list1 = []
    for i in data['地区']:    
        if(str1 in i):
            list1.append(n)
            #new_data = data.drop([n])
        else:
            #print(n)
            pass
        n+=1
    new_data = data.drop(list1) #删除普查小区
    #清洗数据
    data_new=new_data.drop(["机构代码","普通住户","空户","全户外出","全户死亡","全户港澳台居民和外籍人员户","混合户","自主填报户","自主填报率"],axis=1)
    data_new.to_csv(rootdir + SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')


 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(list)):
    data = pd.read_csv(rootdir + list[i])
    jinghua1()


    
