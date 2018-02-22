import HTMLParser

class PlayerPageParser(HTMLParser):

	def handle_starttag(self,tag,attrs):
		if tag=='table' and 'class' in attrs:
			print attrs['class']
			return attrs['class']
		else:
			return ""