a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    #ss4746_Shashwat_Singh-09/23/23
    
    pos_arr = []
    for i in arr:
        if isinstance(i, str):
            pos_arr.append(abs(int(i)))
        else:
            pos_arr.append(abs(i))

    # To Keep the output data type and the input data type same
    if all(isinstance(z, int) for z in arr):
        pos_arr = [int(z) for z in pos_arr]
    elif all(isinstance(z, float) for z in arr):
        pos_arr = [float(z) for z in pos_arr]
    elif all(isinstance(z, str) for z in arr):
        pos_arr = [str(z) for z in pos_arr]

    # Printing the positive output array
    print(pos_arr)

    # Printing output data type
    print("\nType of output data:", type(pos_arr[0]))

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)   
