public class LengthOfLongestSubString {
    public static int lengthOfLongestSubstring(String s) {
        
        
        // "anakanaanakanannkan "
        /* string for current substring
         * string for max length substring
         * look at next char
         * 2 cases: 
         * curr does not contain next char
         *      add next char to curr
         *      update max if curr is large than max
         * curr does contain next char
         *      ** Obersvation : next char will only be present once in curr
         *      remove everything before first instance of next char in curr
         *      add next char
        */

        String curr = "";
        String max = "";

        for(int i=0; i<s.length(); i++) {

            if(!curr.contains("" + s.charAt(i))) {
                curr += s.charAt(i);
                if(curr.length() >= max.length()) {
                    max = new String(curr);
                }
            } else {
                curr = curr.substring(curr.indexOf(s.charAt(i))+1) + s.charAt(i);
            }
        }

        return max.length();
    }
}
