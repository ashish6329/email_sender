from cx_Freeze import setup, Executable
setup(name="e-mail",#name anything
	version="2.0",
	author="Ashish varshney",
	description="you can send email with this programme",
	executables=[Executable(r"/home/lol/Desktop/python programme/emailt.py",
							icon=r"/home/lol/Desktop/python programme/icon.ico",
							shortcutName="send Mail",
							shortcutDir="DesktopFolder")] 
	)




#for windows use command on terminal python filename.py bdist_msi
# for tar file python filename.py bdist_tar
#for mac python filename.py bdist_dumb

