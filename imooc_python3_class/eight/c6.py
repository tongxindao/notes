def print_student_files(name, gender='man', age=19, 
                          college='TJTC'):
    print("My name is " + name)
    print("I'm " + str(age) + ' years old')
    print("I'm a " + gender)
    print("I'm from " + college)

print_student_files('tony', 'man', 19, 'TJTC')
print("=" * 19)
print_student_files('carry')
print("=" * 19)
print_student_files('jerry', age=20)