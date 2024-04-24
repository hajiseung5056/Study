package Java;


class Car implements Runnable{
    int a;

    public void run(){
        System.out.println("message");
    }
}

public class Q22_1_11 {
    public static void main(String[] args) {
        Thread t1= new Thread(new Car());
        t1.start();
    }
}
