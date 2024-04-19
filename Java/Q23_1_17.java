package Java;

abstract class Vehicle{
    String name;
    abstract public String getName(String val);

    public String getName(){
        return "Vehicle name: " + name;
    }
}

class Car extends Vehicle{
    public Car(String val){
        name=super.name=val;
    }
    public String getName(String val){
        return "Car Name : " + val;
    }
    public String getName(byte val[]){
        return "Car Name : " + val;
    }
}



public class Q23_1_17 {
    public static void main(String[] args) {
        Vehicle obj = new Car("Spark");
        System.out.println(obj.getName());
    }
}
