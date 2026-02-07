import os
def ping():
    ping_server = "10.110.110.13"
    response = os.system("ping -n 20 " + ping_server)
    if response == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(ping())