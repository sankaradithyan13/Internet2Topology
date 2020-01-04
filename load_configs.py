import os
import sys
import subprocess
from subprocess import Popen, PIPE

input_path = sys.argv[-1]

direc = os.chdir(input_path)
for f in os.listdir('.'):
	os.chdir(f)
	with open('zebra.conf.sav', 'r') as fd:
		for count,line in enumerate(fd):
			if line != 'interface lo\n':
				if line[:9] == 'interface':
					iface = line
				if line[0] == ' ':
					ip_addr = line
					new_shell = Popen(['../.././go_to.sh', f[-4:]] , stdin=PIPE)
					new_shell.communicate('vtysh  -c "conf t" -c "%s" -c "%s"' % (iface, ip_addr))
	os.chdir('..')
print "Done with configuring interfaces"
for f in os.listdir('.'):
	os.chdir(f)
	with open('ospfd.conf.sav', 'r') as fd:
		for count,line in enumerate(fd):
			if line == 'router ospf\n':
				ospf = line
			if line[:8] == ' network':
					network = line
					new_shell = Popen(['../.././go_to.sh', f[-4:]] , stdin=PIPE)
					new_shell.communicate('vtysh  -c "conf t" -c "%s" -c "%s"' % (ospf, network))
	os.chdir('..')
print "Done with addig OSPF networks"
for f in os.listdir('.'):
	os.chdir(f)
	with open('ospfd.conf.sav', 'r') as fd:
		for count,line in enumerate(fd):
			if line != 'interface lo\n':
				if line[:9] == 'interface':
					iface = line
				if line[:3] == ' ip':
					cost = line
					new_shell = Popen(['../.././go_to.sh', f[-4:]] , stdin=PIPE)
					new_shell.communicate('vtysh  -c "conf t" -c "%s" -c "%s"' % (iface, cost))
	os.chdir('..')
print "Done with configuring OSPF costs"
os.chdir('..')