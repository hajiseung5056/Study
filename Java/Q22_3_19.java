package Java;

public class Q22_3_19 {
    static int[] MarkArray(){
        int[] tempArr = new int[4];
        
        for(int i=0;i<tempArr.length;i++){
            tempArr[i]=i;
        }

        return tempArr;
    }

    public static void main(String[] args) {
        
        int[] intArr;
        intArr= MarkArray();

        for(int i = 0;i<intArr.length;i++){
            System.out.print(intArr[i]);
        }
    }
}
