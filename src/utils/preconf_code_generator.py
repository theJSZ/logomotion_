class JavaPreconfFuncsGenerator:
    """A class for generating preconfigured functions Java code
    """

    def __init__(self):
        pass

    def set_code_generator(self, jcg):
        # pylint: disable=W0201
        self.jcg = jcg

    def get_funcs(self):
        return {"repeat": self._repeat_code(),
                "for": self._for_code()}

    def _repeat_code(self):
        # pylint: disable=W0212
        mangled_name = self.jcg._mangle_java_function_name("repeat")
        java_repeat_code = f"public static void {mangled_name}(double n, Runnable f) {{ \
                    for(int i=0;i<n;i++) {{ \
                        f.run();\
                    }} \
                  }}"
        return java_repeat_code

    def _for_code(self):
        # pylint: disable=W0212
        mangled_for = self.jcg._mangle_java_function_name("for")
        java_for_code = f"public void {mangled_for}(StrVariable placeholder, DoubleVariable start, \
            DoubleVariable limit, Consumer<DoubleVariable> f) {{\
        DoubleVariable new_var = new DoubleVariable(0); \
        for(double itr=start.value;itr<=limit.value;itr++) {{\
            new_var.value = itr;\
            f.accept(new_var);\
            }}\
            }}\
            \
            public void {mangled_for}(StrVariable placeholder, DoubleVariable start, DoubleVariable limit, DoubleVariable step, Consumer<DoubleVariable> f) {{\
                DoubleVariable new_var = new DoubleVariable(0); \
                for (double itr = start.value; itr <= limit.value; itr+=step.value) {{\
                    new_var.value = itr;\
                    f.accept(new_var);\
                }}\
            }}"
        return java_for_code
