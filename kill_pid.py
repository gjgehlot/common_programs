import os
'''The following class/method will kill any program that is currently running
on port listed under list ports_list'''
class kill:
    def __init__(self,ip):
        self.ports_list = [8001,8002] #ports that are currently being used that
        self.ip = ip
        self.kill_port()

    def kill_port(self):
        for val in self.ports_list:
            x = (os.popen('lsof -i -P | grep -i '+self.ip+':'+str(val)).read())
            lnes  = x.split('\n')
            for i in range(0,len(lnes)-1):
                kpid = str(lnes[i].split(' ')[4])
                print('Killing '+kpid)
                os.popen('kill -9 '+kpid)
''' test '''
k = kill(input('Enter the ip address '))
