//Strings
//count upper case letters
public static int countUpper(String s){
    int count = 0;
    for(int i = 0; i < s.length; i++){
        char c = s.charAt(i);
        if (c>='A' && c<= 'Z'){
            count++;
        }
    }
    return count;
}

//remove duplicate characters
public static string removeDuplicates(String s){
    String result = "";
    for(int i = 0; i < s.length(); i++){
        char c = s.charAt(i);
        if(result.indexOf(c) == -1){
            result += c;
        }
    }
    return result;
}

//swap first and last words
public static String swapWords(String s){
    String[] parts = s.split("");
    int last = parts.length - 1;

    String temp = parts [0];
    parts[0] = parts[last];
    parts[last] = temp;
}

//count vowels
    public static int countVowels(String s){
        int count = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++){
            if(vowels.indexOf(s.charAt(i)) != -1){
                count++;
            }
        }
        return count;
    }

    //Remove Digits
    public static String removeDigits(String S){
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(!Character.isDigit(c)){
                result.append(c);
            }
        }
        return result.toString();
    }

    //Alternating Caps
    public static String alternateCaps(String s){
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (i % 2 == 0){
                result.append(Character.toUpperCase(c))
            }
            else {
                result.append(Character.toLowerCase(c));
            }
        }
        return result.toString();
    }


    
