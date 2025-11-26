import re

text = "This is just a test sentence. It'll contain random words! State-of-the-art, B2B, G20, manjulbbalayar@gmail.com stuff you know... pretty dope right?"

pattern = re.compile(r"[a-zA-z']+")
matches = pattern.finditer(text)
for match in matches:
	print(match)
