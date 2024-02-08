class test{
    public static void main(String[] args){
        System.out.println(new Demo().Test());
    }
}
class Demo {
    public int Test(){
        int num1 = 12;
        int num2 = 7;
        while( num2 < 10) {
        num2 = num2 + 2;
        }
        if (num2 < num1 && num2<20){
        num1 = 100;
        }
        else{
        num1 = num2;
        }

        // Calculating product of two numbers
        int product = num1*num2;

        return product;
    }
}