#coding:gbk
"""
目标：编写程序， 完成RPSLS游戏。
RPSLS即Rock-paper-scissors-lizard-Spock，石头剪刀布蜥蜴史波克，来源于“生活大爆炸Big bang”中谢耳朵自创。
规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克等
作者：温晴
日期：2020年4月15日
"""

import random

def name_to_number(name):
	"""
    将游戏对象对应到不同的整数
    """
	if name=="石头":
		return 0# number1=0
	elif name=="史波克":
		return 1# number1=1
	if name=="纸":
		return 2# number1=2
	elif name=="蜥蜴":
		return 3# number1=3
	if name=="剪刀":
		return 4# number1=4
	else:
		print("Error: No Correct Name")
		

	

def number_to_name(number):
	"""
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
	if number==0:
		return "石头"
	elif number==1:
		return "史波克"
	if number==2:
		return "纸"
	elif number==3:
		return "蜥蜴"
	else:
		return "剪刀"
	
	

def rpsls(player_choice):
	"""
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
	print("--------")
	print("您的选择为："+player_choice)
	player_choice_number=name_to_number(player_choice)
	if player_choice_number in (0,1,2,3,4):# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
		comp_number=random.randrange(5)
		print("计算机的选择为:"+number_to_name(comp_number))
		if player_choice_number==comp_number:
			print("您和计算机出的一样呢")# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
		if player_choice_number==0 and  comp_number in (4,3):
			print("您赢了")
		elif player_choice_number==0 and comp_number in (1,2):
			print("机算计赢了")
		if player_choice_number==1 and  comp_number in (4,0):
			print("您赢了")
		elif player_choice_number==1 and  comp_number in (2,3):
			print("计算机赢了")
		if player_choice_number==2 and  comp_number in (1,0):
			print("您赢了")
		elif player_choice_number==2 and  comp_number in (3,4):
			print("计算机赢了")
		if player_choice_number==3 and  comp_number in (1,2):
			print("您赢了")
		elif player_choice_number==3 and  comp_number in (0,4):
			print("计算机赢了")
		if player_choice_number==4 and  comp_number in (2,3):
			print("您赢了")
		elif player_choice_number==4 and  comp_number in (0,1):
			print("计算机赢了")
	else:
		print("--------")

print("欢迎使用RPSLS游戏")
player_choice=input("请输入您的选择:")
rpsls(player_choice)

player_choice=input("请输入您的选择:")
rpsls(player_choice)

player_choice=input("请输入您的选择:")
rpsls(player_choice)

		
	
