# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    
    #        Insert try/except blocks to catch the exception.
    
    try:
        
        age = int(parts[1]) + 1
        
        my_age = int(age)
        
        print(f'{name} {my_age}')

    except ValueError:
        
        print(f'{name} 0')
        
    # Get next line
    parts = input().split()
    name = parts[0]