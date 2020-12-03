# -*- coding:utf-8 -*-
from usb.core import USBError # device is offline or busy when printing
from escpos.exceptions import USBNotFoundError # 实例化的时候
from escpos.printer import Usb
import barcode as Barcode
p = Usb(0x8866, 0x0100, timeout=0, out_ep=0x02)

p.set(align="CENTER")
p.text(" ")
p.text(u"机器编号： xyz-robot-001\n".encode("gbk"))
p.text("------------------------\n")
p.text("2020/09/01  13:01\n\n")
p.set(align="LEFT")
p.text(u"货架编号: xyz081010002\n".encode("gbk"))
p.text(u"\n格口位置:\n\t行数： 3\n\t列数： 3\n".encode("gbk"))
p.set(align="CENTER")
p.image("/home/xyz/code.png")
p.cut()
p.close()

# TODO 启动前检查纸带
# TODO 打印过程中缺纸，如何解决
