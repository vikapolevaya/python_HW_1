from address import Address
from mailing import Mailing

to_address = Address("613152", "Слободской", "Советская", 132, 12)
from_address = Address("613164", "Белая Холуница", "Юбилейная", 34, 2)
cost = 250
track = "Bus216"
mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
