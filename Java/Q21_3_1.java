package Java;

class Connection{
    private static Connection _inst = null;
    private int count = 0;
    static public Connection get(){
        if(_inst == null){
            synchronized(Connection.class){
                if(_inst == null){
                    _inst = new Connection();
                }
            }
        }
        return _inst;
    }
    public void count(){
        count++;
    }
    public int getCount(){
        return count;
    }
}

public class Q21_3_1 {
    public static void main(String[] args) {
        Connection conn1 = Connection.get();
        conn1.count();
        Connection conn2 = Connection.get();
        conn2.count();
        Connection conn3 = Connection.get();
        conn3.count();

        System.out.println(conn1.getCount());
    }
}
