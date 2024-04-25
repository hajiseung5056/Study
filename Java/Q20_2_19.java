package Java;

class A1{
    private int a;
    public void A1(int a){
        this.a = a;
    }
    public void display(){
        System.out.println("a="+a);
    }
}

class B1 extends A1{
    private int a;
    public B1(int a){
        super.A1(a);
        super.display();
    }
}

public class Q20_2_19 {
    public static void main(String[] args) {
        B1 obj = new B1(10);
    }
}
