import subprocess
resp=subprocess.check_output('bcdedit')
#print(type(resp))
resp=resp.decode('utf-8')
#print(type(resp))
#print(resp)
lines=resp.split('\n')
#print(res2)
for line in lines:
     if 'recoveryenabled' in line:
          print(line)