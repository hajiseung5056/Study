package Java;
// static 변수는 모든 객체가 공유
class Static{
    public int a = 20;
    static int b = 0;
}

public class Q23_1_1 {
    public static void main(String[] args) {
        int a;
        a = 10;
        Static.b = a;

        Static st = new Static();

        System.out.println(Static.b++);
        System.out.println(st.b);
        System.out.println(a);
        System.out.println(st.a);
    }
}
