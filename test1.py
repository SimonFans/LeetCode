import json
import string
from collections import defaultdict


def session_id(single_list):

    d = defaultdict(list)

    for i in single_list:
        k = i.split(":")
        #print(k)
        if "sessionid" in k[0]:
            d[k[1]].append(single_list)
    # print sessionid with [......]
    #print(d)
    for k,v in d.items():
        for temp_list in v:
            #print(temp_list)

            for i in temp_list:
                res_list = i.split(" ")

                #print(res_list)
                if "from" in res_list:
                    m=res_list.index("from")
                    #print(str(i)+" = > table_name: "+str(res_list[m+1]))
                    res.append(res_list[m + 1])
                #print(res_list[m+1])
                #Optional for with
                    print(k)
                    print(set(res))

dir1='/Users/simon/Desktop/tabprotosrv_backgrounder_0-2.txt'
dir2='/Users/simon/Desktop/tabprotosrv_vizqlserver_0-0_7.txt'
dir3='/Users/simon/Desktop/tabprotosrv_vizqlserver_0-0_2.txt'


with open(dir1, 'r') as f:
    x = f.readlines()
    res=[]

    count=0
    for item in range(len(x)):


        str_temp=x[item].replace('\\"','"').replace('\r','').replace('\n','').replace('\\r\\n','').replace('\\n','') \
        .replace('(\\n','')

        #print(str_temp)
        single_list=str_temp.split(",")
        for i in single_list:
            #print(single_list)
            k=i.split(":")
            if "class" in k[0]:
                if "redshift" in k[1]:
                    count+=1
                    session_id(single_list)









#print(set(res))



