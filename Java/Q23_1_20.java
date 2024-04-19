package Java;

class Parent{
    int x = 100;

    Parent(){
        this(500);
    }
    Parent(int x){
        this.x = x;
    }
    public int getX(){
        return x;
    }
}

class Child extends Parent{
    int x =4000;
    Child(){
        this(5000);
    }
    Child(int x){
        super(x);
    }
    @Override
    public int getX() {
        return super.getX(); // 부모 클래스의 getX() 메서드를 호출하여 값을 반환합니다.
    }
}

public class Q23_1_20 {
    public static void main(String[] args) {
        Child obj = new Child();
        System.out.println(obj.getX());
    }
}
