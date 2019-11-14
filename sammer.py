import requests
import json
import os
import string
import random

chars= string.ascii_lowercase+ string.digits+'@#$%^*%()'
# print(chars)

password= ''.join(random.choice(chars) for i in range(8))
print(password)