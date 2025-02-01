public class movieRatingSystem {
    public static void main(String[] args) {
        String rate = "" ;
        double rating = 7.8 ;
        long value = Math.round(rating);
        if(value <= 3 && value >= 1) {
            rate = "poor" ;
        } 
        else if(value<= 6 && value >= 4){
            rate = "Average";
        }
        else if(value<= 8 && value >= 7){
            rate = "Good";
        }
        else if(value<= 10 && value >= 9){
            rate = "Excellent";
        }
        double squareRoot = Math.round((Math.sqrt(rating)*100))/100 ;
        double absDiff = Math.abs(value - rating) ;
        double powered = Math.pow(rating, 2) ;
        System.out.println("Rating: " + rating  ) ;
        System.out.println("Feedback: "+ rate);
        System.out.println("Squareroot: "+ squareRoot );
        System.out.println("Absolute Difference: "+ absDiff);
        System.out.println("Rating powred to 2: "+ powered);
         



    }
}
