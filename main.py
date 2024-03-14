# This is a sample Python script.
"""
import Modules.Hi as Hello
import Modules.PrivateIP as pvtIP
"""
# modules


import Modules.Test as tst1
import Modules.server as serv



def print_hi(name):

    print(f'Hi, {name}')

def run():
    # Run the Test.py
    ## Test will check if the private IP is a certain recorded IP address which will be later recorded in a text file
    ### For now this file doesnt exist thus will have to give the private address to it.
    tst1.run()

    # Server start will start the server where the server will listen for transmissions or simply transmit data.
    serv.start()
    cmd = input("Enter Command:") # Implement command library

    while (cmd != 'quit'):
        cmd = input("Enter Input:")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # Hello.print_hello()
    # print(pvtIP.get_pvt_ip())
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
