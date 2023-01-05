public class ZigZagConversion {
    public static void main(String[] args) {
        ZigZagConversion test = new ZigZagConversion();
        System.out.println(test.convert("PAYPALISHIRING", 4));
    }

    public String convert(String s, int numRows) {
        char[] c = s.toCharArray();
        String result = "";
        int charsInSection = 2*(numRows - 1);

        if(numRows == 1) {
            return s;
        }
        
        for(int row = 0; row < numRows; row++) {
            int index = row;

            while(index < c.length) {
                result += c[index] + "";

                if(!(row == 0 || row == numRows -1)) {
                    int firstJump =  charsInSection - 2*row;
                    int secondjump = index + firstJump;

                    if(secondjump < c.length) {
                        result += c[secondjump];
                    }
                }

                index += charsInSection;
            }

    
        }

        return result;
    }
}

