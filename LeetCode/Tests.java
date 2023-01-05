import java.util.LinkedList;

import org.junit.Test;

public class Tests {

    @Test
    public void test_plusMinus() {

        LinkedList<Integer> ints = new LinkedList<>();
        ints.add(1);
        ints.add(-1);
        ints.add(0);
        PlusMinus.plusMinus(ints);
    }

    @Test
    public void test_lengthOfLongestSubString() {
        LengthOfLongestSubString.lengthOfLongestSubstring("dvdf");
    }


}
