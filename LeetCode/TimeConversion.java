public class TimeConversion {

    public static String timeConversion(String s) {
        int length = s.length();
        int hour = Integer.parseInt(s.substring(0, 2));
        String ampm = s.substring(length-2);
        String result = "";
        
        //AM case 
        if(ampm.equals("AM")) {
            // 12am case 
            if(hour == 12) {
                result = "00" + s.substring(2, length-2);
            } else {
                result = s.substring(0, length-2);
            }
        } else {
            //PM case
            if(hour == 12) {
                result = s.substring(0, length-2);
            } else {
                result = 12+hour+s.substring(2, length-2);
            }
        }

        return result;
    }





}
