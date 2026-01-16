//Maps
//Frequency of Words
public static Map<String, Integers> wordCount(List<String> words){
    Map<String, Integer> map = new HashMap<>();
    for(string w : words){
        if(!map.containsKey(w)){
            map.put(w, 1)
        } else {
            map.put(w, map.get(w) + 1)
        }
    }
    return map; 
}

//reverse map
public static Map<String, String> reverseMap(Map<String, String> map){
    Map<String, String> reversed = new HashMap<>();

    for(String key : map.keySet()){
        String value = map.get(key)
        result.put(value, key)
    }
    return result;
}

//invert map
    public static Map<String, String> invert(Map<String, String> map){
        Map<String, String> result = new HashMap<>();
        for (String key : map.keySet()){
            String value = map.get(key);
            result.put(value,key)
        }
        return result;
    }

    // count word lenght
    public static Map<Integer. Integer> countWordLengths(List<String> words){
        Map<Integer, Integer> result = new HashMap<>();
        for(String w : words){
            int len = w.length();
            result.put(len,result.getOrDefualt(len,0) + 1);
        }
        return result;
    }

    //Merge maps by adding
    public static Map<String, Integer> mergeAdd(Map<String, Integer> a, Map<String, Integer> b) {
        
        Map<String, Integer> result = new HashMap<>();

        for (String key : a.keySet()) {
            result.put(key, a.get(key));
        }

        for (String key : b.keySet()) {
            result.put(key, result.getOrDefault(key, 0) + b.get(key));
        }

        return result;
    }