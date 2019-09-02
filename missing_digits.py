n=input("Enter the number ")
print("missing digits are:",end=" ")
for i in range(10):
	if str(i) in n:
		pass
	else:
		print(i,end=" ")
		