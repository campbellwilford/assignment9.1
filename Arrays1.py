## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
step_one_array = np.full((4, 3), 2)
print('Step One:', step_one_array)
print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
step_two_array = np.arange(0, 120, 10).reshape(3, 4)
print('Step Two:', step_two_array)
print() 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
step_three_array = step_two_array.reshape(4, 3)
print('Step Three:', step_three_array)
print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
step_four_array = step_three_array * 3
print('Step Four:', step_four_array)
print()

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
#result_step_five = np.dot(step_one_array, step_two_array.T)  
#print('Step Five:', result_step_five)
## This errored out... why?
print()
#the numbers of columns has to match the number of rows
## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
step_six_array = step_one_array * step_three_array
print('Step Six:', step_six_array)
## this worked! why?
print()



