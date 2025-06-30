onechina = "!!ONE CHINA!!"
print("!!ONE CHINA!!".center(52))
class Address:
def init(self, name, street, city, state, pincode):
self.name = name
self.street = street
self.city = city
self.state = state
self.pincode = pincode

def display(self):
    print(f"{self.name}\n{self.street}\n{self.city}\n{self.state}\n{self.pincode}")
addr = Address("Vishnu Babalsure".center(51), "FC Road".center(51), "Pune".center(51), "Maharashtra".center(51) ,"411001".center(51))
addr.display()

ContactNo = "9503496775"
print("9503496775".center(50))

def print_line(length=50):
print("__"*length)

print_line(50)

name = "Nilesh"
print("name:", name)

print_line(50)

from datetime import datetime
cashier="biller"
print("cashier:",cashier)
billno=1
print("billno:",billno)
print(datetime.now().time())

print_line(50)

dis1={"chillichican:",350.0, "non vegntrian:",325.0}
print("item \t Qty \tprices")
def _print_line(length=50):
print("__"*length)
_print_line(80)
print("chillichican \t 1 \t 350.0")
print("non vegntrian\t 1\t 325.0")

print_line(50)
dis2={"container charge:",30.0,"CGST2.5%:",17.6,"SGST2.5%:",17.6}

print("totalQty:2\t 675.0")
print("container charge\t 30.0")
print("CGST2.5% \t 17.6")
print("SGST2.5% \t 17.6")

print_line(50)

totalgrand = 675.0 + 30.0 + 17.6 + 17.6
print("totalgrand:", totalgrand)

print_line(50)

print("THANK YOU!&Visit Again".center(70))
