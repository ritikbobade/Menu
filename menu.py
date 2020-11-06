import os
import getpass
os.system("tput setaf 3")
print("                                       Welcome to my menu              ")
os.system("tput setaf 7")
print("                                       -------------------                   ")


password=getpass.getpass("Enter your Password")
if password!="ritik":
	print("Access Denied")
	exit()


while True:
	print("""
	\n
	Press 1:Big Data Hadoop
	Press 2:AWS Cloud
	Press 3:Machine Learning
	Press 4:Docker
	Press 5:DSA
	Press 6.Python
	Press 7.Partitions
	Press 8.Exit
	""")
	ch=input("Enter your choice")
	if int(ch)==1:
		print("""
		Press 1:To open hdfs-site.xml file
		Press 2:To open core-site.xml file
		Press 3: To start namenode
		Press 4: To start datanode
		Press 5: To run jps 
		""")
		nm=input("Enter your choice")
		if int(nm)==1:
			os.system("cd /etc/hadoop; vi hdfs-site.xml")
		elif int(nm)==2:
			os.system("cd /etc/hadoop; vi core-site.xml")
		elif int(nm)==3:
			os.system("hadoop-daemon.sh start namenode")
		elif int(nm)==4:
			os.system("hadoop-daemon.sh start datanode")
		elif int(nm)==4:
			os.system("jps")
		else:
			print("Invalid choice")
	elif int(ch)==2:
		print("""
		Press 1:To Configure aws 
		Press 2:To Launch a Ec2 Instance
		Press 3:To Create a EBS storage
		Press 4:To Creaet a S3 bucket
		""")
		aw=input("Enter your Choice")
		if int(aw)==1:
			os.system("aws configure")
		elif int(aw)==2:
			os.system("aws ec2 start-instances help")
		elif int(aw)==3:
			os.system("aws ec2 create-volume help")
		elif int(aw)==4:
			os.system("aws s3 help")
		else:
			print("Invalid choice")
		
	elif int(ch)==3:
		print("""
		Press 1: To launch jupyter notebook
		Press 2: To install numpy
		Press 3: To install pandas
		""")
		ml=input("Enter your choice")
		if int(ml)==1:
			os.system("jupyter notebook --allow-root")
		elif int(ml)==2:
			os.system("pip3 install numpy")
		elif int(ml)==3:
			os.system("pip3 install pandas")
		else:
			print("Invalid choice")
	elif int(ch)==4:
		print("""
		Press 1:To see running docker containers
		Press 2:To run Ubuntu:18.10
		Press 3:To run ubuntu:14.04
		Press 4:To run ubuntu:20.10
		Press 5:Exit		
		""")
		dc=input("Enter your choice")
		if int(dc)==1:
			os.system("docker ps")
		elif int(dc)==2:
			os.system("docker run -it ubuntu:18.10")
		elif int(dc)==3:
			os.system("docker run -it ubuntu:14.04")
		elif int(dc)==4:
			os.system("docker run -it ubuntu:20.10")
		else:
			print("Invalid choice")
	elif int(ch)==5:
		print("""
		Press 1:To check time taken by your code
		Press 2:Check memory of your code
		Press 3:Exit
		""")	
		da=input("Enter your Choice")
		if int(da)==1:
			cd=("Type your command to run your code")
			os.system("time {}".format(cd))
		elif int(da)==2:	
			print("Enter your desitnation location whose memory you want 					to check e.g. /home/Desktop/menuy.py")
			mm=input()
			os.system("df {}".format(mm))
		else:	
			print("Invalid choice")
	elif int(ch)==6:
		print("""
		Press 1:To check python version
		Press 2.To run python interpreter
		Press 3.Exit
		""")
		ph=input("Enter your choice")
		if int(ph)==1:
			os.system("python3 --version")
		elif int(ph)==2:
			os.system("python3")
		else:
			print("Invalid choice")

	elif int(ch)==7:
		print("""
		Press 1:To check disk information
		Press 2:To partition in a particular disk
		Press 3: To check the mount state
		""")
		pr=input("Enter your Choice")
		
		if int(pr)==1:
			os.system("fdisk -l")
		elif int(pr)==2:
			ds=input("Enter the disk name")
			os.system("fdisk /dev/{}".format(ds))
		elif int(pr)==3:	
			os.system("df -h")
		else:
			print("Invalid choice")
	else:
		exit()
