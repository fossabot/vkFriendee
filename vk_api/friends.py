# -*- coding: utf-8 -*-
"""
:authors: python273, ractyfree
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2019 python273
"""

from .exceptions import VkApiError




class VkFriends(object):
	""" Wrapper for working with Friends method

	:param vk object :class 'VkApi'
	"""
	def __init__(self, vk):
		self.vk = vk

	def add_friend(self, user_id, text="Hey I want you to add me in friends", follow=0):
		values = {
		'user_id': user_id,
		'text': text,
		'follow': follow
		}
		response = self.vk.method("friends.add", values)
		return response

	def getSuggestions(self, _filter="mutual", count=500, offset=0, fields="", name_case="nom"):
		values = {
		'filter': _filter,
		'count': count,
		'offset': offset,
		'fields': fields,
		'name_case':name_case
		}
		response = self.vk.method("friends.getSuggestions", values)
		return response



class VkFriendsError(VkApiError):

	def __init__(self, error):
	    self.error_code = error['error_code']
	    self.message = error['message']

	def __str__(self):
	    return '[{}] {}'.format(self.error_code, self.message)