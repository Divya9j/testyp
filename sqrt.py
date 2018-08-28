# This program calculates the square root.
inp = float(input("Please enter Number: "))
guess = inp/2;
accuracy = 0.01;
iteration=0;
while abs(inp-(guess**2)) > accuracy :
    guess = (guess+(inp/guess))/2;
    print("Iteration : ",iteration," Current Guess : ",guess);
    iteration=iteration+1;
print("original number is : ",inp);
print("Square root of number is : ", guess);

