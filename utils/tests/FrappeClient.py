import frappe
import requests
import json
import utils

class FrappeClient:
	user = 'Guest'
	def __init__(self, url, user=None):
		self.url = url
		self.session = requests.Session()
		self.session.headers.update({'Accept': 'application/json'})
		self.set_user(user)

	def set_user(self, user=None):
		if user == 'Guest':
			return
		if user:
			self.user = user
		token = utils.create_user_access_token(self.user)
		self.session.headers.update({'Authorization': token})

	def __api_url(self, uri):
		return '{host}/api/method/{uri}'.format(
			host=self.url,
			uri=uri
		)

	def get_api(self, uri, data={}):
		return self.session.get(self.__api_url(uri), json=data)

	def post_api(self, uri, data={}):
		return self.session.post(self.__api_url(uri), json=data)