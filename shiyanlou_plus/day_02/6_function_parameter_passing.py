def connect(ipaddress, port=22):
    print("IP: ", ipaddress)
    print("port: ", port)


def connect1(ipaddress, *ports):
    print("IP: ", ipaddress)
    for port in ports:
        print("port: ", port)


def connect2(ipaddress, ports):
    print("IP: ", ipaddress)
    print("ports: ", ports)
    ipaddress = "10.10.10.1"
    ports.append(8080)


def hello(*, name="User"):
    print("Hello", name)


def f(a, data=[]):
    data.append(a)
    return data


def g(a, data=None):
    if data is None:
        data = []
    data.append(a)
    return data


connect("192.168.1.1", 22)
print("=" * 30)
connect(22, "192.168.1.1")
print("=" * 30)
connect(port=22, ipaddress="192.168.1.1")
print("=" * 30)
connect("192.168.1.1")
print("=" * 30)
try:
    hello("shiyanlou")
except TypeError:
    print("TypeError: hello() takes 0 positional\narguments but 1 was given")
print("=" * 30)
hello(name="shiyanlou")
print("=" * 30)
print(f(1))
print("=" * 30)
print(f(2))
print("=" * 30)
print(f(3))
print("=" * 30)
print(g(1))
print("=" * 30)
print(g(2))
print("=" * 30)
connect1("192.168.1.1")
print("=" * 30)
connect1("192.168.1.1", 22, 23, 24)
print("=" * 30)
connect1("192.168.1.1", 22)


if __name__ == "__main__":
    ipaddress = "192.168.1.1"
    ports = [22, 23, 24]
    print("Before connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)
    print("In connect:")
    connect2(ipaddress, ports)
    print("After connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)
