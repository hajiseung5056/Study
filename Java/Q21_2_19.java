package Java;

public class Q21_2_19 {
    public static void main(String[] args) {
        Q21_2_19 a1 = new Q21_2_19();
        Q21_2_19 a2 = new Q21_2_192();
        System.out.println(a1.sun(3,2)+a2.sun(3,2));
    }
    int sun(int x, int y){
        return x + y;
    }
}

class Q21_2_192 extends Q21_2_19{
    int sun(int x, int y){
        return x - y + super.sun(x,y);
    }
}