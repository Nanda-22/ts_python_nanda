# validation IP Address
ipv4="256.27.0.4"  
#ipv4="192.168.0.6"

ips=ipv4.split(".")#["10","27","0","4"]
print(ips)
c=0
flag=0
for i in ips:
    if int(i)>=256 or int(i)<0:
        flag=1
        break
        
if flag==0:
    print("{} is valid ip".format(ipv4))
else:
    print("{} is not valid ip".format(ipv4))
