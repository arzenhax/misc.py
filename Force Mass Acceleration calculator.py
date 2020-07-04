#This code calculates a trains mass, acceleration, and distance.
#The explanations come after the code

train_mass = 22680
train_acceleration = 10
train_distance = 100

#^These are the variables

def get_force(mass, acceleration):
  return mass * acceleration

#This code is used to get the force by multiplying mass and acceleration.

train_force = get_force(train_mass, train_acceleration)

#This code calculates the force specifically for the train using the variables at the start of the code.

print("The GE train supplies", train_force, "Newtons of force.")

#This prints out a sentence including the variable of "train_force"

def get_energy(mass,c=3*10**8):
    return mass * c**2

#Here, "c" is a constant which is the speed of light.
#The equation to get the engergy is mass multiplied by the speed of light.

bomb_mass = 1

bomb_energy = get_energy(bomb_mass)

#Here is another variable that uses the "get_energy" function.
#The input of the function "get_energy" is the "bomb_mass", which, according to the line of code above it, is equal to 1

print("A 1kg bomb supplies", bomb_energy, "Joules.")

#Here we just print out this sentence. Remember that strings are in quotes, and variables are not.
#They are also seperated with commas

#Now we are going to call a function, and call another function that has already been defined.
#This is the bulk of programming, where you call tiny functions to other bigger functions.

def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration) 
  return force * distance

#Work is equal to Force multiplied by Distance, so we use the "get_force(mass,acceleration)" function that is higher up this code to, get the force,
#and then save it in this "get_work(mass,acceleration,distance)" function as "force" to use in the equation of force times distance.

train_work = get_work(train_mass,train_acceleration,train_distance)

#Here we input the variables of the train into the "get_work()" function and save it as the variable "train_work"

print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")

input("Press Enter to continue...")


