public class MaximumOddBinaryNumber {
    public static void main(String[] args) {
        String s = new String("010");
        var l = s.toCharArray();

        int left = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) {
            if (l[i] == '1') {
                swap(l, i, left);
                left++;
            }
        }
        swap(l, left-1, length-1);

    }

    static public char[] swap(char[] s, int i, int j) {
        var temp = s[j];
        s[j] = s[i];
        s[i] = temp;
        return s;
    }
}
