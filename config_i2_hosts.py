import os
import sys
import subprocess
from subprocess import Popen, PIPE

new_shell = Popen(['./go_to.sh', 'NEWY-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig newy 4.101.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'NEWY-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.101.0.2 newy')

new_shell = Popen(['./go_to.sh', 'CHIC-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig chic 4.102.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'CHIC-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.102.0.2 chic')

new_shell = Popen(['./go_to.sh', 'WASH-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig wash 4.103.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'WASH-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.103.0.2 wash')

new_shell = Popen(['./go_to.sh', 'ATLA-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig atla 4.104.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'ATLA-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.104.0.2 atla')

new_shell = Popen(['./go_to.sh', 'KANS-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig kans 4.105.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'KANS-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.105.0.2 kans')

new_shell = Popen(['./go_to.sh', 'HOUS-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig hous 4.106.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'HOUS-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.106.0.2 hous')

new_shell = Popen(['./go_to.sh', 'SALT-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig salt 4.107.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'SALT-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.107.0.2 salt')

new_shell = Popen(['./go_to.sh', 'LOSA-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig losa 4.108.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'LOSA-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.108.0.2 losa')

new_shell = Popen(['./go_to.sh', 'SEAT-host'] , stdin=PIPE)
new_shell.communicate('sudo ifconfig seat 4.109.0.1/24 up')
new_shell = Popen(['./go_to.sh', 'SEAT-host'] , stdin=PIPE)
new_shell.communicate('sudo route add default gw 4.109.0.2 seat')

print "Done with adding all host interfaces"
