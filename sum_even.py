#A four-digit integer is given. Find the sum of even digits in it.
x = 4538
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = x
#Create a variable "sum_even" and assign it 0.
sum_even = 0
#Find the sum of the even digits in the variable "var_int".
sum_even = (var_int//1000%2)*(var_int//1000)+(var_int//100%2)*(var_int//100-var_int//1000*10)+(var_int//10%2)*(var_int//10-var_int//100*10)+(var_int%2)*(var_int-var_int//10*10)

