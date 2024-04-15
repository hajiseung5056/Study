package Java;

public class Q23_2_2 {
    public static void main(String[] args) {
        int m=4620;
        int a= m / 1000;
        int b= m % 1000 / 500;
        int c= m % 500 / 100;
        int d= m % 100 / 10;

        System.out.println(a); // 천원짜리      4장출력
        System.out.println(b); // 오백원짜리    1개출력
        System.out.println(c); // 백원짜리      1개출력
        System.out.println(d); // 십원짜리      2개출력

    }
}
