variable = "global"
def func_outer():
    variable = "enclosing outer local"
    def func_inner():
        variable = "enclosing inner local"
        def func_local():
            variable = "local"
            print(variable)
        func_local()
    func_inner()
 
func_outer()  # prints 'local' defined in the innermost function
print(variable)  # 'global' level variable holds its value