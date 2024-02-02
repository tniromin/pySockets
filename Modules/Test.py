import Modules.PrivateIP as tpvtIP


def test(func, value):
    result = func
    if result == 1:
        print(value+": Pass")
    else:
        print(value+": Fail")


def run():
    test(tpvtIP.test_pvt_ip(), "Get Private Address")


# run()
