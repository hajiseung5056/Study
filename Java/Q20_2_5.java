package Java;

class Parent1{
    public void show(){
        System.out.println("Parent");
    }
}

class Child1 extends Parent1{
    public void show(){
        System.out.println("Child");
    }
}


public class Q20_2_5 {
    public static void main(String[] args) {
        Parent1 pa = new Child1();
        pa.show();
    }
}
