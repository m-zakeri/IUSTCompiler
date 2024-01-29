

class AddressCodeConverter():

    @staticmethod
    def array_initializer(i, exp1, exp2,temp):
        return f"\t\t{temp} = sizeOf{i}\n\t\t{temp}={temp}*{exp1}\n\t\t{temp}= &{i}+{temp}\n\t\t*{temp}={exp2}"

    @staticmethod
    def tmp_array(tmp, exp1, exp2):
        return [f'\t\t{tmp}=sizeOf({exp1})' ,f'\t\t{tmp}={tmp}*{exp2}' , 
                f'\t\t{tmp}= &{exp1}+{tmp}']
                
