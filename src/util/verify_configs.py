import configs
import requests
import validators
import re
import src.log as log

class VerifyConfigs:
	def __init__(self, exclude: list = [""]):
		"""
		Returns an object that verifies each of the items in the config file

		To exclude certain checks pass the names of the configs in a list

		:param (list) exclude: List of items to exclude from being checked

		:return (bool) Wether or not the bot should be allowed to start up or not.
		"""
		self.validated = True
		self.exclude = exclude
		self.logger = log.fetch_logger()
		self.check_alpha = re.compile('^([a-z]\s)*$', re.IGNORECASE)

		self.verify()

	def verify(self):
		"""
		Runs the verifications

		:return (None)
		"""
		if "BOT_NAME" not in self.exclude:
			self.verify_name(case=configs.BOT_NAME)
		if "URL" not in self.exclude:
			self.verify_url(case=configs.URL)
		if "IMG_URL" not in self.exclude:
			self.verify_image(case=configs.IMG_URL)
		if "PREFIX" not in self.exclude:
			self.verify_prefix(case=configs.PREFIX)
		if "SERVER" not in self.exclude:
			self.verify_server(case=configs.SERVER)
		if "SECRET" not in self.exclude:
			self.verify_secret(case=configs.SECRET)

	def verify_name(self, case: str) -> bool:
		"""
		Verifies the name in configs.BOT_NAME

		:return (bool) Whether the name was successfully validated or not
		"""
		if not self.check_alpha(case):
			self.logger.critical("Failed to validate BOT_NAME") 
			self.validated = False
			return False
		
		self.logger.log("Successfully validated BOT_NAME")
		return True

	def verify_url(self, case: str) -> bool:
		"""
		Verifies the URL in configs.URL

		:return (bool) Whether the url was successfully validated or not
		"""
		if not validators.url(case):
			self.logger.critical("Failed to validate URL: URL entered is not a valid URL")
			return False

		page_request = requests.get(case, allow_redirects=True)
		if page_request.status_code != 200:
			self.logger.critical("Failed to validate URL: Could not find page URL")
			return False
		
		self.logger.log("Successfully validated URL")
		return True

	def verify_image(self, case: str) -> bool:
		"""
		Verifies the image URL in configs.URL_IMG

		:return (bool) Whether the image url was successfully validated or not
		"""
		case.removesuffix('/')
		file_type = case.split('.')[-1]

		if file_type not in configs.SUPPORTED_IMG_TYPES:
			self.logger.critical("Image File type not supported, reverting to default")
			return False

		file_request = requests.get(case, allow_redirects=True)
		if file_request.status_code != 200:
			self.logger.critical("Could not find image on the web, reverting to default")
			return False

		self.logger.log("Successfully validated IMG_URL")
		return True

	def verify_prefix(self, case: str) -> bool:
		if case == "":
			self.logger.error("PREFIX Error please check")
			self.validated = False
			return False
		
		self.logger.debug("Successfully validated PREFIX")
		return True
	
	def verify_server(self, case: str) -> bool:
		"""
		Verifies the server name in configs.SERVER

		:return (bool) Whether the server name was successfully validated or not
		"""

		if not self.check_alpha(case):
			self.logger.critical("Failed to validate SERVER") 
			self.validated = False
			return False
		
		self.logger.log("Successfully validated SERVER")
		return True

	def verify_secret(self, case: str) -> bool:
		"""
		Verifies the server secret in configs.SECRET

		:return (bool) Whether the secret was successfully validated or not
		"""
		if len(case) != 70:
			self.logger.critical("SECRET error: Secret is not 70 characters long")
			return False
		
		self.logger.log("Successfully validated SECRET")
		return True
	