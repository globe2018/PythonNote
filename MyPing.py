Python 如何 ping
背景
最近需要监测一个服务器的运行状态。

因为服务器部署在两地，网络抖动对业务的影响很大，所以要在网络抖动情况严重时做一些警报。

实现方法有很多种，最终选择了使用 Python 来实现这样的功能。

实现
Python 实现 ping 有几种方法：

1、自己实现 ping
2、调用系统 ping
3、使用 Python 模块

自己实现 ping
ping 的原理就是发送一份 ICMP 回显请求报文给目标主机，并等待目标主机返回ICMP回显应答。

如果想要自己写，可以自己控制发报文，这里推荐一篇博客大家可以自行前去学习：点我去学习

调用系统 ping
这个就没什么复杂的，就是调用系统的 ping，但是如果有跨平台使用的需求，要区分好系统平台，windows 要特殊处理一下，可以参考如下代码：

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
使用 Python 模块
一般大家也不会自己造轮子，尤其是对于 Python 这种轮子众多的，我们只要从中选择好用的就可以。

这里推荐大家几个挺不错的 ping 模块。

ping3
代码地址：https://github.com/kyan001/ping3

功能很强大，使用简单，缺点也比较明显——需要 root 权限。

Note that ICMP messages can only be sent from processes running as root.
需要 root 权限运行的 process 才能发送 ICMP 数据。

>>> from ping3 import ping, verbose_ping
>>> ping('example.com')  # Returns delay in seconds.
0.215697261510079666

>>> verbose_ping('example.com')  # Ping 4 times in a row.
ping 'example.com' ... 215ms
ping 'example.com' ... 216ms
ping 'example.com' ... 219ms
ping 'example.com' ... 217ms
1
2
3
4
5
6
7
8
9
MultiPing
代码地址：https://github.com/romana/multi-ping/

话说一个大牛，觉得目前的工具都不好用，然后就自己写了一个。

特点是可以以较小的资源同时 ping 多个地址。

from multiping import MultiPing

# Create a MultiPing object to test three hosts / addresses
mp = MultiPing(["8.8.8.8", "youtube.com", "127.0.0.1"])

# Send the pings to those addresses
mp.send()

# With a 1 second timout, wait for responses (may return sooner if all
# results are received).
responses, no_responses = mp.receive(1)

1
2
3
4
5
6
7
8
9
10
11
12
TCPing
代码地址：https://github.com/zhengxiaowai/tcping

TCP 实现的 ping，与 ICMP 的 ping 原理不同，但反应网络是否连通、延迟多少的功能是一样的。

还有另外一个优点，也是最终被我选用的优点，不需要 root 权限。

from tcping import Ping

def ping_check():
    ping = Ping('192.168.0.116', 80, 60)
    ping.ping(10)

    ret = ping.result.rows
    for r in ret:
        print(r)

    ret = ping.result.raw
    print(ret)

    ret = ping.result.table
    print(ret)


if __name__ == '__main__':
    ping_check()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
该有的统计什么的也都是有的，而且很好用。

➜  ~ tcping api.github.com -c 3 --report
Connected to api.github.com[:80]: seq=1 time=237.79 ms
Connected to api.github.com[:80]: seq=2 time=237.72 ms
Connected to api.github.com[:80]: seq=3 time=258.53 ms

+----------------+------+-----------+--------+--------------+----------+----------+----------+
|      Host      | Port | Successed | Failed | Success Rate | Minimum  | Maximum  | Average  |
+----------------+------+-----------+--------+--------------+----------+----------+----------+
| api.github.com |  80  |     3     |   0    |   100.00%    | 237.72ms | 258.53ms | 244.68ms |
+----------------+------+-----------+--------+--------------+----------+----------+----------+
1
2
3
4
5
6
7
8
9
10
行了，就先分享到这里了，大家可以根据自身情况灵活选择，每个库都试一试，总能找到满足你需求的。

祝大家搬砖顺利。
————————————————
版权声明：本文为CSDN博主「Bottle」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhyl8157121/article/details/109002584
  
