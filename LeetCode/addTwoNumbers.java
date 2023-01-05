class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            
            int sum = findSum(l1) + findSum(l2);
            int[] digits = extractDigits(sum);
            ListNode result = arrayToLN(digits, 0, new ListNode());
            
            return result;
            
        }

        int findSum(ListNode node) {
            int result = 0;
            int i=0;
            while(node.next != null) {
                result += node.val * 10^i;
                node = node.next;
            }

            return result;
        }

        ListNode arrayToLN(int[] arr, int index, ListNode result) {
            
            if(index >= arr.length) {
                return result;
            }

            result.val = arr[index];
            index++;
            result.next = arrayToLN(arr, index, result);

            return null;
        }

        int[] extractDigits(int i) {
                
            int[] result = {};

            int index = 0;
            int power = 1;
            while(i > 0) {
                int digit;
                digit = i / (10^power);
                i -= digit;
                result[index] = digit / (10^(power-1));
                index++;
            }

            return result;
        }

    // 342
    // 342%10 -> 2/1 -> 2
    // 342 - result from above * 1 -> 340
    // 340%100 -> 40/10 -> 4
    // 340 - result from above * 10 -> 300
    // 300%100 -> 300/100 -> 3
    // 300 - result from above * 100 ->0



}