import java.util.Comparator;
import java.util.List;

class Result {

    public static void miniMaxSum(List<Integer> arr) {
        // Write your code here
        arr.sort(Comparator.naturalOrder());
        long minSum = 0;
        long maxSum = 0;

        for(int i=0; i<arr.size()-1; i++) {
            minSum += arr.get(i);
        }

        for(int i=1; i<arr.size(); i++) {
            maxSum += arr.get(i);
        }
        
        System.out.println(minSum + " " + maxSum);
        }

        
}