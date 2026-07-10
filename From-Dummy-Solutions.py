#Beginner Approach


#----------Dummy 1
def dummy_function_power(base, exponent = 2):
    return base ** exponent

print(dummy_function_power(3))  
print(dummy_function_power(3, 3))  

#Can be manually replace the exponent
#ex.
print(dummy_function_power(3, exponent=4))

# Output: 9 27 81 

#----------Dummy 2
i = 7 

if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i += 3

print(i) 
 # Output: 8


 #----------Dummy 3 

def dummy_summarize(*args, **kwargs):
    print("[args] Tuple Values:", args)
    print("[kwargs] Key value pair:", kwargs)

dummy_summarize(1, 2, 4, name="Norwegian", age=19)

 #----------Dummy 4




 #----------Dummy 5





 #----------Dummy 6