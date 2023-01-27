import subprocess
def update():
    process = subprocess.Popen("git checkout . && git pull ",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (use,nouse)=process.communicate()
    if "Already up to date" in use.decode():
        print("[+] it is updated")
    else:
        print("[+] updating....")
        print(use)
print("pass1")
update()
