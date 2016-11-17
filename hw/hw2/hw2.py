#csc321
#hw2
#blahhh


#1. What is the IP configuration for your PythonAnywhere server?

"""
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 22:00:0b:01:86:88 brd ff:ff:ff:ff:ff:ff
    inet 10.147.16.72/24 brd 10.147.16.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::2000:bff:fe01:8688/64 scope link
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:99:84:4d:88 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
"""

#2. What are the MAC addresses for these interfaces?

"""
lo: 00:00:00:00:00:00
eth0: 22:00:0b:01:86:88
docker0: 02:42:99:84:4d:88
"""

#3. What are all the IPv4 addresses associated with these interfaces?

"""
lo: 127.0.0.1/8
eth0: 10.147.16.72/24
docker0: 172.17.0.1/16
"""


#4. What is the IP subnet associated with each of these addresses?

"""
lo: 127.0.0.0/9, 127.128.0.0/9
eth0: 10.147.16.0/25, 10.147.16.128/25
docker0: 172.17.0.0/17, 172.17.128.0/17
"""

#5. What is the netmask of each of these IP subnets?

"""
lo: 255.128.0.0
eth0: 255.255.255.128
docker0: 255.255.128.0
"""

#6. How many IP addresses are available in each of these subnets?

"""
a lot of IP adrresses. definitely in the thousands range. (i could not figure
out how to count the endless flood of ip addresses on my screen after i tried
to view each subnet's hosts. or perhaps i could, but i procrastinated, so yay.)
"""

#7. Do any of the interfaces stand out? If so, do some research into what they might imply regarding the structure of PythonAnywhere.

"""
none of these interfaces stand out to me, and i dont think it's me being lazy
or unwilling to do research.
"""

#8. Are any of these IP addresses public? If not, prove it. If so, prove it.

"""
I dont think any of these addresses are public. I tested it in an ipython 3.5
console. when I asked are any of these hosts are global, it returned 'False',
therefore I think it's safe to conclude that none of my IP addresses are public.
"""