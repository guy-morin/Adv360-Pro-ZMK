import string

def string2macro(macro_name, s):

    bindings = "<" + " ".join(list(map(lambda x: "&kp "+ string.capwords(x), s))) + ">"
    head = f"""
    {macro_name}: {macro_name} {{
    compatible = "zmk,behavior-macro";
    label = "{macro_name}";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <10>;
    bindings = {s};
  }}; 
    """.format(macro_name=macro_name, s=bindings)
    return head
    
    
    
if __name__ == "__main__":
    macro_main = string2macro("macro_main", s="if __name__ == \"__main__\"")
    macro_class = string2macro("macro_class", s="class ")
    macro_def = string2macro("macro_def", s="def ")
    print(macro_main)
    print(macro_class)
    print(macro_def)