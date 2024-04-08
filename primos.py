def is_primo(value):
    if value == 1:
        return False
    num_div = 2
    while num_div < value: 
        if value % num_div == 0:
            return False
        num_div += 1
    return True
      
    





