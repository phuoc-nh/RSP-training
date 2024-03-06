public class MinimumLength {
    public static void main(String[] args) {
        System.out.println(minimumLength("bbbbb"));;
    }

    static public int minimumLength(String s) {
        int i = 0;
        int j = s.length()-1;

        char[] charString = s.toCharArray();
//        System.out.println(charString);
        while (i < j && charString[i] == charString[j]) {
            while (i < s.length()-1 && charString[i] == charString[i+1]) {
                i++;
            }

            while (j >0 && charString[j] == charString[j-1]) {
                j--;
            }

            i++;
            j--;
        }

//        System.out.println(">>>iii" + i);
//        System.out.println(">>>jjj" + j);
        if (i > j) {
            return 0;
        }
        return j - i + 1;
    }
}
