## 第九关通关脚本

by [小拿](justinli.ljt@gmail.com) 2012-11-16

    昨晚逛V2EX(http://v2ex.com/t/52444)，看到这个游戏，通关后，发现第九关还是挺有意思，于是整理了一下思路。

### 原理

* 第九关打开后是一大长串的二进制字符串，我们先忽略其中的空位。
* 观察这个串，发现每个8位二进制位的第一位全部为 **0** ，我们知道非扩展的 **ASCII编码** 正好有 128 个，因而可以尝试用 **ASCII编码** 进行解码。
* 可以知道的是，解码后，我们必然得到一个很长的字符串。通过抽样发现，这些字符串是无意义的字符组合，并不是明文的形式。于是想到网络经常使用的加密明文的 **base64编码**，尝试用其进行解码试试。
* 回到我们第一个问题，二进制编码中有很多空位，解码前要将这些空位补齐才可以。通过肉眼观察，也没看出什么规律来，于是想到尝试分别用 **0** 和 **1** 填充，看看效果如何。
* 尝试发现，填充 **1** 后，转换成的 ascii 字符串恰恰可以通过 **base64** 进行解码，于是可以肯定我们的尝试是正确的。
* 在 **base64** 解码后，得到一堆乱码（包含可见字符和不可见字符），肯定后面的问题不是字符编码的问题了。对于这种乱码，我们可以尝试通过不同的文件格式来尝试。
* 我第一次尝试的是 **.tar.gz** 后缀，惊喜的是，解压成功了。里面是一张 **jpg** 的照片。后面的事情，你懂的 **:)**

### 脚本

1. 将网页显示的二进制字符串复制粘贴到文本文件 __password.txt__。
2. 调用 __the_ninth_level.py__ 脚本：

   `python the_ninth_level.py password.txt`

3. 脚本生成result.tar.gz压缩包，解压得到 cang.jpg 图片，打开即得到通过密码。




p.s. [光棍节程序员闯关秀](http://segmentfault.com/game/)

