public class Solution {
    public String reverseString(String s) {
        if(s == null || s.equals("")) return s;
        char[] arrChar = s.toCharArray();
        for (int i = 0, j = arrChar.length-1; i <= j; i++, j--) {
            char temp = arrChar[i];
            arrChar[i] = arrChar[j];
            arrChar[j] = temp;
        }
        return new String(arrChar);
    }
}

//copy from Shans.Xia. it spends 2ms, beats 90.17% of javasubmissions. surprising Java 0_o