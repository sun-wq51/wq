#coding:gbk
"""
Ŀ�꣺��д���� ���RPSLS��Ϸ��
RPSLS��Rock-paper-scissors-lizard-Spock��ʯͷ����������ʷ���ˣ���Դ�ڡ������ըBig bang����л�����Դ���
�����ǣ������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ���˵�
���ߣ�����
���ڣ�2020��4��15��
"""

import random

def name_to_number(name):
	"""
    ����Ϸ�����Ӧ����ͬ������
    """
	if name=="ʯͷ":
		return 0# number1=0
	elif name=="ʷ����":
		return 1# number1=1
	if name=="ֽ":
		return 2# number1=2
	elif name=="����":
		return 3# number1=3
	if name=="����":
		return 4# number1=4
	else:
		print("Error: No Correct Name")
		

	

def number_to_name(number):
	"""
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
	if number==0:
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	if number==2:
		return "ֽ"
	elif number==3:
		return "����"
	else:
		return "����"
	
	

def rpsls(player_choice):
	"""
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
	print("--------")
	print("����ѡ��Ϊ��"+player_choice)
	player_choice_number=name_to_number(player_choice)
	if player_choice_number in (0,1,2,3,4):# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
		comp_number=random.randrange(5)
		print("�������ѡ��Ϊ:"+number_to_name(comp_number))
		if player_choice_number==comp_number:
			print("���ͼ��������һ����")# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
		if player_choice_number==0 and  comp_number in (4,3):
			print("��Ӯ��")
		elif player_choice_number==0 and comp_number in (1,2):
			print("�����Ӯ��")
		if player_choice_number==1 and  comp_number in (4,0):
			print("��Ӯ��")
		elif player_choice_number==1 and  comp_number in (2,3):
			print("�����Ӯ��")
		if player_choice_number==2 and  comp_number in (1,0):
			print("��Ӯ��")
		elif player_choice_number==2 and  comp_number in (3,4):
			print("�����Ӯ��")
		if player_choice_number==3 and  comp_number in (1,2):
			print("��Ӯ��")
		elif player_choice_number==3 and  comp_number in (0,4):
			print("�����Ӯ��")
		if player_choice_number==4 and  comp_number in (2,3):
			print("��Ӯ��")
		elif player_choice_number==4 and  comp_number in (0,1):
			print("�����Ӯ��")
	else:
		print("--------")

print("��ӭʹ��RPSLS��Ϸ")
player_choice=input("����������ѡ��:")
rpsls(player_choice)

player_choice=input("����������ѡ��:")
rpsls(player_choice)

player_choice=input("����������ѡ��:")
rpsls(player_choice)

		
	
