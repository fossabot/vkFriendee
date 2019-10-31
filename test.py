from vkfriendee import *
import getopt



"""
With this script you can easily run VkFriendee with command line arguments:

python <this script.py> --login(-l) *login* --pass(-p) *pass* --verbose(-v)

"""


if __name__ == "__main__":

	
	optlist, args = getopt.getopt(sys.argv[1:], "l:p:v:h",["login=", "password=", "verbose", "help"])
	print(sys.argv)
	for key, value in optlist:
		if key in ("--login", "-l"):
			login = value
		if key in ("--password", "-p"):
			password = value
		if key in ("--verbose", "-v"):
			logging.basicConfig(level=logging.INFO, stream=sys.stdout)
		if key in ("--help", "-h"):
			print("Commands list:\n--login(-l)\n--password(-p)\n--verbose(-v)\n--help(-h)")

	
	vk = VkApi(login, password)
	wrk = Friends(vk)
	wrk.startFriending()
	