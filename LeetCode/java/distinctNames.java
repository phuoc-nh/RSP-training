import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

public class distinctNames {
    public static void main(String[] args) {
        String[] ideas = new String[]{"egxxmj","lwyfu","ejekpwt","aaupak","mkkduac","rqagl","uzpnrk","respojrw","tkgbbbapux","g","xm","zrpzncxd","xsepajvsbf","whgvrydqkq","v","ursybjwty","kgphomgzp","aty","obwciqob","splyrvposr","nmozkef","owuu","ubiighh","fbcu","emgrmsdv","hvryqejbw","vruduliz","c","edkagr","gsbofx","tss","xafac","eclgdcuv","stjsqvdq","zy","majsjubk","vkwbkh","iugeprqr","h","q","bggxhcu","o","wekksqc","a","woj","xxe","ipdhtkquzq","viiaf","sid","vagjrp","ibk","rsjiczl","uaveojflk","fvbnsdt","bjrqnfmlb","azkgyifss","e","bmcx","x","rctt","vxtxec","m","cixir","rvyv","gkbgfhk","feuqbiql","aefdzxti","rqfw","pcccaixl","pwkkcpji","avdsqb","fbxwxhbtht","vsckcqpyyk","k","kecbog","eoyda","d","hdsfchzy","dt","ntt","hxtrvitasv","kpazfnk","cydztwrfn","cbedyerin","aol","kzpm","fomkn","rrnynb","hceyws","earibvxue","f","zeyds","uk","thchullucg","tpjcus","sjpsamldub","mvhkclv","cjn","z","uwsksad","ricknuassw","thubaxua","bpfornqm","iaahd","euktdmsrd","bqmm","rwpldnn","s","enlm","yn","idjy","kek","tea","y","quvv","fxnzafpj","lpxcic","ukkkcepgmh","ga","qhqr","wwply","gqwck","urg","qacoulgiy","nscx","etjqfeo","dgio","mxtqyi","kuuuvy","vq","hlornknbl","yk","il","bnmyqvnfb","otrwu","ermb","avyj","ghincf","pvwwne","iduic","hzkglzjho","uqjswxrlrw","vfnacbho","iydd","jlyz","j","bmdxlde","jmk","ygbnp","gw","hjkc","gvxf"};
        distinctNames distinctNames = new distinctNames();
        distinctNames.distinctNames(ideas);
    }

    public long distinctNames(String[] ideas) {
        // HashMap<Character, List<String>> uniqueOriginalNames = new HashMap<>();
        // int res = 0;

        
        // for (String idea: ideas) {
        //     if (uniqueOriginalNames.containsKey(idea.charAt(0))) {
        //         uniqueOriginalNames.get(idea.charAt(0)).add(idea.substring(1));
        //     } else {
        //         List<String> list = new ArrayList<>();
        //         list.add(idea.substring(1));
        //         uniqueOriginalNames.put(idea.charAt(0), list);
        //     }
        //     var a = uniqueOriginalNames.get("x");
        // }
        // System.out.println(">>>>>> " + uniqueOriginalNames);
        // for (Character key1: uniqueOriginalNames.keySet()) {
        //     for (Character key2: uniqueOriginalNames.keySet()) {
        //         if (key1.equals(key2)) continue;
        //         int intersection = 0;
        //         // System.out.println("key2" + uniqueOriginalNames.get(key2) + key2);
        //         // System.out.println("key1" + uniqueOriginalNames.get(key2) + key1);
        //         for (String word: uniqueOriginalNames.get(key1)) {
        //             // System.out.println("word " + word);
        //             if (uniqueOriginalNames.get(key2).contains(word)) {
        //                 intersection += 1;
        //             }
        //         }

        //         // System.out.println("+++" +intersection);

        //         int diff1 = uniqueOriginalNames.get(key1).size() - intersection;
        //         int diff2 = uniqueOriginalNames.get(key2).size() - intersection;

        //         res += diff1 * diff2;
        //     }
        // }
        // // System.out.print(">>>>>> " + res);
        // return res;

        HashSet<String>[] initialGroup = new HashSet[26];
        System.out.println(">>>>" + initialGroup);
        for (int i = 0; i < 26; ++i) {
            initialGroup[i] = new HashSet<>();
        }
        for (String idea : ideas) {
            initialGroup[idea.charAt(0) - 'a'].add(idea.substring(1));
        }
        
        // Calculate number of valid names from every pair of groups.
        long answer = 0;
        for (int i = 0; i < 25; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                // Get the number of mutual suffixes.
                long numOfMutual = 0;
                for (String ideaA : initialGroup[i]) {
                    if (initialGroup[j].contains(ideaA)) {
                        numOfMutual++;
                    }
                }

                // Valid names are only from distinct suffixes in both groups.
                // Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                answer += 2 * (initialGroup[i].size() - numOfMutual) * (initialGroup[j].size() - numOfMutual);
            }
        }
        
        return answer;
    }
}
