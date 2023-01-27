import subprocess
def update():
    process = subprocess.Popen("git checkout . && git pull ",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(process)
print("pass")
update()
