#read the hostname, without the trailing newline. Requires the hostname to be written into a file named .host within the CWD/PWD. 
f = open(".host",'r')
name = f.read().strip()
f.close()
#read the dovecot.conf configuration file from the current working directory.
f.close()
f = open('dovecot.conf','r')
txt = f.read()
f.close()
#modify the file by replacing the word 'studio' with the hostname of the current computer.
f = open('dovecot.conf','w')
txt = txt.replace('studio',name)
f.write(txt)
f.close()
#read the main.cf configuration file from the current working directory.
f = open('main.cf','r')
txt = f.read()
f.close()
#replace 'studio' with the hostname of the current machine.
f = open('main.cf','w')
txt = txt.replace('studio',name)
f.write(txt)
f.close()

