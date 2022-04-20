package programmers;

import java.util.HashMap;
import java.util.Map;

public class 전화번호_목록 {

    public boolean solution(String[] phone_book) {
        Trie trie = new Trie();
        for (String number : phone_book) {
            if (!trie.add(number)) {
                return false;
            }
        }
        return true;
    }

    class Node {
        boolean hasEnd = false;
        String alpha;
        Map<String, Node> children = new HashMap<>();

        public Node(String alpha) {
            this.alpha = alpha;
        }
    }

    class Trie {

        Node head = new Node("head");

        public boolean add(String s) {
            Node cur = head;
            for (int i=0; i<s.length(); i++) {
                String c = String.valueOf(s.charAt(i));
                if (!cur.children.containsKey(c)) {
                    cur.children.put(c, new Node(c));
                }
                cur = cur.children.get(c);
                if (cur.hasEnd) {
                    return false;
                }
            }
            cur.hasEnd = true;
            if (cur.children.size() > 0) {
                return false;
            }
            return true;
        }
    }
}
