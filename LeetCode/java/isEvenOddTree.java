import java.util.LinkedList;
import java.util.Queue;

//  * Definition for a binary tree node.

class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList();
        q.offer(root);
        int index = 0;

        while (!q.isEmpty()) {
            int size = q.size();

            if (index % 2 == 0) {
                // increasing order odd numbers only
                var prev = Integer.MIN_VALUE;
                for (int i = 0; i < size; i++) {
                    var cur = q.poll();
                    if (cur.val % 2 == 0) {
                        return false;
                    }

                    if (cur.val <= prev) {
                        return false;
                    }

                    if (cur.left != null) {
                        q.offer(cur.left);
                    }
                    if (cur.right != null) {
                        q.offer(cur.right);
                    }

                    prev = cur.val;
                }
            }
            else {
                // decreasing order even numbers only
                var prev = Integer.MAX_VALUE;
                for (int i = 0; i < size; i++) {
                    var cur = q.poll();
                    if (cur.val % 2 == 1) {
                        return false;
                    }

                    if (cur.val >= prev) {
                        return false;
                    }

                    if (cur.left != null) {
                        q.offer(cur.left);
                    }
                    if (cur.right != null) {
                        q.offer(cur.right);
                    }

                    prev = cur.val;
                }
            }

            index += 1;
        }

        return true;
    }
}