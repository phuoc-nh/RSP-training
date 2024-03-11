import java.util.Arrays;

public class CustomSortString {
    public static void main(String[] args) {

    }

    public String customSortString(String order, String s) {
        int lenS = s.length();
        Character[] res = new Character[lenS];
        for (int i = 0; i < lenS; i++) {
            res[i] = s.charAt(i);
        }

        // Define the custom comparator
        Arrays.sort(res, (c1, c2) -> {
            // The index of the character in order determines the value to be sorted by
            return order.indexOf(c1) - order.indexOf(c2);
        });

        // Return the res
        String resString = "";
        for (Character c: res) {
            resString += c;
        }
        return resString;
    }
}
