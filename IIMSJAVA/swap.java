public class swap {
    public static void main(String[] args) {
        int a = 125 ;
        int b = 456 ;
        System.out.println("Before -> a:" + a + " b:"+ b);
        a = b - a  ;
        b = b - a ;
        a = a +b ;
        System.out.println("After -> a:" + a + " b:"+ b);
    }
}
