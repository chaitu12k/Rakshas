from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING10 = getenv("STRING10")
API_ID = getenv("20194031")
API_HASH = getenv("e070877a18b6ad44631469b702082ed0")
BIO_MESSAGE = getenv("BIO")
SUDO = list(map(int, getenv("SUDO").split()))
