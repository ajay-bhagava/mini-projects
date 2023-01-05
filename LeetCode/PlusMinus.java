import java.util.List;

public class PlusMinus {

    public static void plusMinus(List<Integer> arr) {
        double positives = 0;
        double negatives = 0;
        double zeros = 0;
        int size = arr.size();

        for (Integer i : arr) {
            if (i > 0) {
                positives++;
            } else if (i < 0) {
                negatives++;
            } else {
                zeros++;
            }
        }

        System.out.println(positives / size);
        System.out.println(negatives / size);
        System.out.println(zeros/size);
    }

    



}
