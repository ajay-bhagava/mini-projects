class Solution {
    int numbers[] = {1000,500,100,50,10,5,1};
    String numerals[] = {"M", "D", "C", "L", "X", "V", "I"};

    public String intToRoman(int num) {
        String result = "";
        int i = 0;
        while(num >= numbers[i]) {
            num -= numbers[i];
            result += numerals[i];
            if(num == 0) {break;}
            if(num < numbers[i]) {
                i++;                
            }
        }
        cleanUpNumeral(result);
        return result;
    }

    public String cleanUpNumeral(String str) {
        char letters[] = str.toCharArray();
        int repetitions = 0;
        String result = "";
        if(str == "") {
            return str;
        } else {
            result = "" + letters[0];
        }
        
        
        

        for(int i=1; i<letters.length; i++) {
            if(letters[i] == letters[i-1]) {
                repetitions +=1;
            } else {
                repetitions = 0;
            }
            result += letters[i];
            if(repetitions >= 3) {
                String convertedResult = "" + letters[i] + letters[i-4];
                result = result.substring(0, i-4) + convertedResult;
            }

        }

        return result;
    }

}