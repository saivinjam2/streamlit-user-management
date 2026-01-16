public class MyPractice {

    // 🔹 Fields
    private String name;
    private int[] numbers;
    private List<String> words;

    // 🔹 Constructor
    public MyPractice(String name) {
        this.name = name;
        this.numbers = new int[] {1, 2, 3};
        this.words = new ArrayList<>();
    }

    // 🔹 Sample method #1 (Strings)
    public int countVowels(String input) {
        if (input == null) return 0;
        int count = 0;
        input = input.toLowerCase();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if ("aeiou".indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }

    // 🔹 Sample method #2 (Lists)
    public void addWord(String w) {
        if (w != null) {
            words.add(w);
        }
    }

    // 🔹 Sample method #3 (Maps)
    public Map<String, Integer> countWordLengths(List<String> items) {
        Map<String, Integer> result = new HashMap<>();
        for (String s : items) {
            result.put(s, s.length());
        }
        return result;
    }

    // 🔹 Sample method #4 (2D arrays)
    public int sum2D(int[][] grid) {
        int sum = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                sum += grid[r][c];
            }
        }
        return sum;
    }


    //Remove all vowels
    public static String removeAllVowels(String s){
        String vowels = "aeiouAEIOU"
        StringBuilder out = new StringBuilder();
        for(int i = 0; i<s.length(); i++){
            if(vowels.indexOf(s.charAt(i))== -1){
                out.append(s.charAt(i));
            }
        }
        return out.toString();
    }

    //Repeat Characters
    public static String repeatChars(String s, int n){
        StringBuilder out = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            for (int k = 0; k < n; k++){
                out.append(s.charAt(i))
            }
        }
        return out.toString();
    }

    //count words
    public static int countWords(String s){
        if(s.trim().isEmpty){
            return 0;
        }
        String[] parts = s.trim().split("\\s+");
        return parts.length();
    }

    //Lists
    //Filter even numbers
    public static List<Integer> filterEven(List<Integer> nums){
        List<Integer> result = new ArrayList<>();
        for (n : nums){
            if (n % 2 == 0){
                result.add(n);
            }
        }
        return result; 
    }

    //Find Longest Word
    public static String longestWord (List<String> words){
        if(words.size()==0){
            return null;
        }
        String longest = words.get(0);
        for(String w : words){
            if(w.length() > longest.length()){
                longest = w;
            }
        }
        return longest;
    }

    //Swap Elements
    public static void swap(List<Integer> nums, int i, int j){
        int temp = nums.get(i);
        nums.set(i, nums.get(j));
        nums.set(j, temp);
    }

    //Map Solutions
    //Freequency Counter
    public static Map<Character, Integer> charFreq(String s) {
        Map<Character,Integer> map = new HashMap<>();
        for(int i = 0; i<s.length(); i++){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        return map;
    }



}
