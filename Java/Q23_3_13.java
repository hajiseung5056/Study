package Java;

class Person{
    private static String name;
    public Person(String val){
        name=val;
    }
    public static String get(){
        return name;
    }
    public void print(){
        System.out.println(name);
    }
}

public class Q23_3_13 {
    public static void main(String[] args){
        Person obj = new Person("Kim");
        obj.print();
    }
}
