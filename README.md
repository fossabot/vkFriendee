# VkFriendee - Make friends easily


### What is this?
With this script you can easily start gaining count of your friends in VK. Just follow the instructions below and feel free to ask anything.

### Who it can helps?
It can helps anybody who wants to automatically get suggested friends which are recommended by VK itself. Also there is a big effort for webmasters who want to advertise something in VK more politely for alghoritms.

### Features:
- Auto accepting of incoming friendship requests.
- Auto sending friendship requests to recommended friends
- Perfect logging of script activity
- Elaborate stats view

## Requirements:
- Python 3+

## How to install
1. First of all you need to fork/clone/download this repository
2.  Secondly you need to python been installed properly.
3.  Thirdly you need to execute script with basic executor('main.py).
With command-line looks-like: 

		python main.py --login "YOUR_NUMBER" --password "YOUR_PASSWORD" --verbose

Then you'll see the verbose output


## Coding stuff
### vkFriendee.py
Consists of class 'Friends' and has only one public function, all other funcs are for private usage, you can use them, but it's not supported.

Public functions definition:

	def startFriending(self)
	"""Allows you to start the main script's alghoritm"""


### main.py
This script allows you to basically execute vkFriendee class.
Full command-line:
> --login(-l) - Accepts here a login for VK. It must be your telephone number<br>
--password(-p) - Accepts here a password for VK. It must be your password for the account.<br>
--verbose(-v) - Switcher for verbose output<br>
--help - ...

## Credits
vk_api: https://github.com/python273/vk_api
