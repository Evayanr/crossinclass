with open('report.txt',encoding='utf-8')as report:#表头字段
    line_1=report.readline()
    s_sort1=line_1.split()
    s_sort1.insert(0,'名次')
    s_sort1.append('总分')
    s_sort1.append('平均分')
    result_1=' '.join(s_sort1)+'\n'
    print(result_1)
    with open('result.txt','w+',encoding='utf-8')as results:#表头写入
        results.writelines(result_1)
with open('report.txt',encoding='utf-8')as report:#数据处理
    next(report)#从第2行开始
    lines=report.readlines()#读取report的数据
scores=[]
for l in lines:
    s=l.split() 
    sum_raw=0 #计算合计数、平均数
    for data in s[1:]:
        sum_raw=sum_raw+int(data)
    s.append(str(sum_raw))
    s.append(str(round(sum_raw/len(s[2:]),1)))
    #print(s)
    scores.append(s)
#print(scores)
scores_sort=sorted(scores,key=lambda x:x[-2],reverse=True)#按合计数降序排列
scores_sort.insert(0,['平均'])#增加平均值行
#print(scores_sort)
for column in range(1,(len(scores_sort[1]))):#计算各列平均值
    sum_column=0
    avg_column=0
    #print(len(scores_sort[1]))
    for s_sort in scores_sort[1:]:
        sum_column=sum_column+float(s_sort[column])
        avg_column=round(sum_column/len(scores_sort[1:]),1)
        #print(s_sort)
    #print(sum_column,avg_column)
    scores_sort[0].append(str(avg_column))
#print(scores_sort)
for s_sort in scores_sort:
    s_sort.insert(0,str(scores_sort.index(s_sort)))#加入名次
    s_sortswap=s_sort[0:2]+['不及格'if float(x)<60 else x for x in s_sort[2:] ]#替换60分以下为不及格
    #print(s_sort)
    #print(s_sortswap)
    result_n=' '.join(s_sortswap)+'\n'
    print(result_n)
    with open('result.txt','a',encoding='utf-8')as results:#数据写入
        results.writelines(result_n)



