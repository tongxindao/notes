result = [(a, b) 
            for a in ['a', '1', 1, 2] 
            for b in ['1', 3, 4, 'b'] 
            if a != b]

print(result)
