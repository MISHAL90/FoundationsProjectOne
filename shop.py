####################### DO NOT MODIFY THIS CODE ########################
menu = {
	"original cupcake": 2,
	"signature cupcake": 2.750,
	"coffee": 1,
	"tea": 0.900,
	"bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name ="second cup"
signature_flavors = ['egg','tofe','baniple']
order_list = []


def print_menu():
	"""
	Print the items in the menu dictionary.
	"""
	# your code goes here!
	for item in menu:
		print("- '%s' (KD %s)" %(item, menu[item]))


def print_originals():
	"""
	Print the original flavor cupcakes.
	"""
	print("Our original flavor cupcakes (KD %s each):" % original_price)
	# your code goes here!
	for flavor in original_flavors:
		print (flavor)


def print_signatures():
	"""
	Print the signature flavor cupcakes.
	"""
	print("Our signature flavor cupcake (KD %s each):" % signature_price)
	# your code goes here!
	for sign in signature_flavors:
		print (sign)


def is_valid_order(order):
	"""
	Check if an order exists in the shop.
	"""
	# your code goes here!
	if order in menu :
		return True
	else:
		for flavor in original_flavors:
			if flavor == order :
				return True
		for flavor in signature_flavors:
			if flavor == order :
				return True
	return False



def get_order():
	"""
	Repeatedly ask customer for order until they end their order by typing "Exit".
	"""
	order_list = []
	# your code goes here!
	print("What is your order? Type Exit to end")
	while True:
		order=input()
		if order=="Exit":
			break
		elif is_valid_order(order):
			order_list.append(order)
			print("order added")
		else:
			print("order does't exists")


	return order_list


def accept_credit_card(total):
	"""
	Return whether an order is eligible for credit card payment.
	"""
	# your code goes here!
	if total >= 5 :
		print("Your order accepts credit card payment")
	else:
		print (" your order does not accept_credit_card")


def get_total_price(order_list):
	"""
	Calculate and return total price of the order.
	"""
	total = 0
	# your code goes here!
	for order in order_list:
		if order in menu :
			total+= menu[order]
		else:
			for flavor in original_flavors:
				if flavor == order :
					total+= original_price
			for flavor in signature_flavors:
				if flavor == order :
					total+= signature_price

	return total


def print_order(order_list):
	"""
	Print the order of the customer.
	"""
	print()
	print("Your order is: ")
	# your code goes here!
	for order in order_list:
		print(order)

	total = get_total_price(order_list)
	print("your total is %s KD" % total)
	accept_credit_card(total)
