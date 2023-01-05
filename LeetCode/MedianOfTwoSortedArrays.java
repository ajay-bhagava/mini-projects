import java.util.Arrays;

public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // High level
            // Merge the arrays 
            // Find median of merged arrays 


            int[] merged = new int[nums1.length + nums2.length]; 
            Arrays.sort(merged);

            int size = merged.length;
            if(size % 2 == 0) {
                double middle = (double) merged[size/2];
                double next = (double) merged[size/2 + 1];
                return (middle+next)/2;
            } else {
                return (double) merged[size/2];
            }
    }
} 