//Scanner
//Read integers until -1
public static int sumUntilStop(Scanner sc){
    int sum = 0;
    int value = sc.nextInt();
    while(value != -1){
        sum+= value;
        vlaue = sc.nextInt();
    }
    return sum;
}
 
//Scanner
    //Count words until STOP
    public static int countUntilStop(Scanner sc) {
        int count = 0;
        while (sc.hasNext()) {
            String word = sc.next();
            if (word.equals("STOP")) {
                break;
            }
            count++;
        }
        return count;
    }

    //Sum Integers
    public static int sumInts(Scanner sc) {
        int sum = 0;
        while (sc.hasNextInt()) {
            sum += sc.nextInt();
        }
        return sum;
    }

    //First Word of each line
    public static List<String> firstWords(Scanner sc){
        List<String> result = new ArrayList<>();
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            String lineScan = new Scanner(line)
            if(lineScan.hasNext){
                result.add(lineScan.next());
            }
            lineScan.close();
        }
        return result;
    }