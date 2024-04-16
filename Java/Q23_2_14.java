package Java;
    // '=='는 주소비교, 'equals'는 내용비교
public class Q23_2_14 {
    public static void main(String[] args) {
        String str1 = "Programming";
        String str2 = "Programming";
        String str3 = new String("Programming");

        System.out.println(str1==str2);
        System.out.println(str1==str3);
        System.out.println(str1.equals(str3));
        System.out.println(str2.equals(str3));

    }
}
