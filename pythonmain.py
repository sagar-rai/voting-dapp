import user
import admin

def main():
	c=int(input('''Enter Choice
					1. Admin app
					2. User app
					3. Exit'''))
	if c==1:
		admin.main()
	elif c==2:
		user.main()
	else:
		exit()

if __name__=="__main__":
	main()