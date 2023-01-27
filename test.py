import subprocess
def update():
    process = subprocess.Popen("git checkout . && git pull ",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (use,nouse)=process.communicate()
    print(use)
print("pass1")
update()
