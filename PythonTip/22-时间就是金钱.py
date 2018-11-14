# coding=utf-8

"""
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
"""
st, et = "00:00:00", "00:00:10"
# #################_Submitted code as follows_###########################
import datetime


st = datetime.datetime.strptime(st, "%H:%M:%S")
et = datetime.datetime.strptime(et, "%H:%M:%S")

print (et - st).seconds
