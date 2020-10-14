#define a function
def flow_control(k):

	#define a string based on the value of k
	if(k==0):
		s = "variable k = %d equals 0." % k

	elif(k==1):
		s = "variable k = %d equals 1." % k

	else:
		s = "variable k = %d does not equal 0 or 1." % k

	only_zero(k)
	print(s)

def only_zero(k):
	if(k==0):
		print("We're just evaluating k== ", k)

#define a main function
def main():

	#declare an integer
	i = 0

	#try flow control for i=0,1,2
	flow_control(i)

	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

#run the program
if __name__ == '__main__':
		main()
