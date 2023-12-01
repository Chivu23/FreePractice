# VARIABLES
nice_day = "everyday"
kid = 'joy'

# DATA TYPES
year_int = 2023
kg_float = 62.3
nr_par_bool = True
nr_impar_bool = False
exe_string = "Have a color day!"

# BUILT-IN FUNCTION "TYPE()" & "PRINT()"
print(type(year_int))  # ---> <class 'int'>
print(type(exe_string))  # ---> <class 'str'>

# LIST  ---> ORDERED (the elements are kept in the order in which they were added)
#       ---> MUTABLE (elements CAN be modified, added or deleted)
list_demo = ["good_energy", 23, 23.23, "False", False, True]

# DICTIONARY ---> UNORDERED (the elements are NOT kept in the order in which they were added)
# >KEY:VALUE< ---> MUTABLE (elements CAN be modified, added or deleted)
demo_dictionary = {
    2023: "this year",
    2024: "next year",
    "happy": "new year",
    True: "day"
}

# SET  ---> UNORDERED (the elements are NOT kept in the order in which they were added)
#      ---> MUTABLE (the elements CAN be modified, added or deleted)
kids = {"Maria", "Peter", "Bobby"}

# TUPLE ---> ORDERED (the elements are kept in the order in which they were added)
#       ---> IMMUTABLE (the elements can NOT  be modified, add or deleted)
demo_tuple = ("sun", "dance", "smile")

print(list_demo)        # ---> ['good_energy', 23, 23.23, 'False', False, True]
print(demo_dictionary)  # ---> {2023: 'this year', 2024: 'next year', 'happy': 'new year', True: 'day'}
print(kids)             # ---> {'Maria', 'Bobby', 'Peter'}
print(demo_tuple)       # ---> ('sun', 'dance', 'smile')



