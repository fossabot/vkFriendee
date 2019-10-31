from vk_api import *
import logging
import sys
import time
import random

class Friends:
	""" Class for auto-friending with possible friends from your town

	:param vk: object :class:VkApi
	:param count: int :Count of friends to add
	:param city: str :City 

	"""
	TIMEOUT = 30
	TIMEOUT_THREESHOLD = 20 # After which accepted count of friends we have to wait with TIMEOUT(mins)

	def __init__(self, vk, count=1500, city="Default"):

		if isinstance(vk, VkApi):
			vk.auth()
			self.__vk = vk.get_api()
		else:
			logging.error("'vk' object is not an instance of VkApi class")
			sys.exit(-1)

		self.count = count
		self.city = city
		logging.debug("Friends class initialized")


	def __getSuggestions(self, count=100):
		""" Returns list of suggested friendss
			:param count :int

		"""
		return self.__vk.friends.getSuggestions(count=count, fields="city")['items']

	def __getRequests(self):
		""" Returns list of incoming requests
		"""
		return self.__vk.friends.getRequests(out=0)['items']

	def __add(self, user_id):
		""" Sends request to user to add him in friends list
		:param user_id :int
		"""
		return self.__vk.friends.add(user_id=user_id)

	def __getMyFriends(self):
		""" Returns count of friends that you have
		"""
		return self.__vk.friends.get()['count']

	def __log(self, aled, ladd):
		logging.info("\nFriends to add: %d\nFriends already added: %d\nFriends left to add: %d\nFriends Currently: %d\nFriendship requests sent in total: %d\nPercent of users accepted the request: %f\n", self.count, aled, ladd, self.__getMyFriends(), self.srstf, ((aled/self.srstf)*100) if self.srstf != 0 else 0.0)
	
	def __isBlocked(self, user_id):
		""" Returns BOOL if user_id is blocked
		:param user_id :int
		"""
		try:
			if self.__vk.users.get(user_ids=user_id)[0]['deactivated'] == 'banned':
				return True
		except KeyError:
			pass
		return False
	
	def __addAllRequests(self):
		logging.info("Accepting all incoming friend requests")
		for x in self.__getRequests():
			if not self.__isBlocked(x):
				self.__add(x)
				time.sleep(random.randint(3,8))


	def __addNewFriends(self, count=5):
		logging.info("Sending requests to add in friends")
		sugs = self.__getSuggestions()
		i = 0
		for x in range(0, count):
			sug = random.choice(sugs)
			try:
				if sug['is_closed'] == False and ((sug['city']['title'] == self.city) if self.city != "Default" else True):
					self.__add(sug['id'])
					logging.info("Sent a request to %d", sug['id'])
					self.srstf = self.srstf + 1
					time.sleep(random.randint(20, 40))
			except KeyError:
				pass
		
			


	def startFriending(self):
		logging.info("Start of auto-friending script.")
		bfrs = self.__getMyFriends()
		ttfrs = bfrs + self.count

		self.srstf = 0
		aled = 0
		ladd = self.count
		
		self.__log(aled, ladd)

		while True:
			self.__addAllRequests()

			if self.__getMyFriends() >= ttfrs:
				"""
				If we've reached needed amount of friends then we break the loop
				"""
				break

			self.__addNewFriends(count=5)
			

			ladd = ttfrs - self.__getMyFriends()
			aled = self.__getMyFriends() - bfrs
			self.__log(aled, ladd)
			sl = random.randint(300, 600)
			logging.info("Sleeping now %dsecs before starting new iteration", sl)
			time.sleep(sl)