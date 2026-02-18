def print_info(**kwargs):
	for key,value in kwargs.items():
		print(f"{key}:{value}")
print_info(name="alice",age=30,city="new york")