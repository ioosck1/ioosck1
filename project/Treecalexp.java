import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

class Node {
    
    String data;
    Node left, right;

    public Node(String data) {
        this.data = data;
        left = right = null;
    }
}

public class Main {

    public static boolean isOperator(String ch) {
        return (ch.equals("+") || ch.equals("-") || ch.equals("*") || ch.equals("/") || ch.equals("^"));
    }

    public static Node expressionTree(String[] equation, int notation) {
        Stack<Node> st = new Stack<Node>();
        try {
            switch (notation) {
                case 1:  // Prefix
                    for (int i = equation.length - 1; i >= 0; i--) {
                        st = PrePost_fix(equation[i], st,notation);
                    }
                    break;
                case 2:  // Infix
                    Node t1, t2, temp, node;
                    for (int i = 0; i < equation.length; i++) {
                        if (Arrays.asList(equation).contains("(") && Arrays.asList(equation).contains(")")) {
                            st = findbracket(equation[i], st);
                        } else {
                            if (!isOperator(equation[i])) {
                                temp = new Node(equation[i]);
                                st.push(temp);
                            } else {
                                temp = new Node(equation[i]);

                                t1 = st.pop();
                                i++;
                                node = new Node(equation[i]);
                                st.push(node);
                                t2 = st.pop();

                                temp.left = t1;
                                temp.right = t2;

                                st.push(temp);
                            }
                        }
                    }
                    break;
                case 3:  // Postfix
                    for (int i = 0; i < equation.length; i++) {
                        st = PrePost_fix(equation[i], st,notation);
                    }
                    break;
                default:
                    return null;
            }
        } catch (Exception e) {
            System.out.println("\nAn error occurred : " + e.getMessage());
            e.printStackTrace();
        }
        return st.pop();
    }

    public static void display(Node root) {
        if (root != null) {
            display(root.left);
            System.out.print(root.data);
            display(root.right);
        }
    }

    public static Stack<Node> PrePost_fix(String equation, Stack<Node> st,int notation) {
        Node t1, t2, temp;
        if (!isOperator(equation)) {
            temp = new Node(equation);
            st.push(temp);
        } else {
            temp = new Node(equation);

            t1 = st.pop();
            t2 = st.pop();
            if (notation == 1){
                temp.left = t1;
                temp.right = t2;
            }
            else {
                temp.left = t2;
                temp.right = t1;
            }

            st.push(temp);
        }
        return st;
    }
    
    public static Stack<Node> findbracket(String equation, Stack<Node> st) {
        int limit = 0;
        Node t1, t2, temp, node;
        if (equation.equals(")")) {
            for (int j = st.size() - 1; j >= 0; j--) {
                node = st.get(j);
                if (node.data.equals("(")) {
                    limit = j;
                    break;
                }
            }
            for (int k = st.size() - 1; k > limit; k--) {
                node = st.get(k);
                if (isOperator(node.data) && node.left == null && node.right == null) {
                    st.remove(node);
                    temp = new Node(node.data);
                    t1 = st.pop();
                    t2 = st.pop();
                    temp.left = t2;
                    temp.right = t1;
                    if (st.peek().data.equals("(")) {
                        st.pop();
                    }
                    st.push(temp);
                    k--;
                }
            }
        } else {
            temp = new Node(equation);
            st.push(temp);
        }
        return st;
    }

    public static int calculateTree(Node Tree) {
        if (Tree == null) {
            return 0;
        } else if (Tree.left == null && Tree.right == null) {
            return Integer.parseInt(Tree.data);
        }
        int left = calculateTree(Tree.left);
        int right = calculateTree(Tree.right);
        if (Tree.data.equals("+")) {
            return left + right;
        } else if (Tree.data.equals("-")) {
            return left - right;
        } else if (Tree.data.equals("*")) {
            return left * right;
        } else {
            return left / right;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Select;
        String input;
        String[] equation;
        String[] choice = {"Prefix", "Infix", "Postfix"};
        System.out.println("Tree Calculate Expression");
        for (int i = 0; i < choice.length; i++) {
            System.out.printf("%d.%s\n", i + 1, choice[i]);
        }
        System.out.println("4.Exit program");
        System.out.print("Your choice number is : ");
        Select = sc.nextInt();
        sc.nextLine();
        try {
            if (Select > 0 && Select <= 3) {
                System.out.printf("Your %s : ", choice[Select - 1]);
                input = sc.nextLine();
                equation = input.split(" ");
                Node r = expressionTree(equation, Select);
                System.out.print("Display at inorder : ");
                display(r);
                System.out.println("\nsum of equations : " + calculateTree(r));
            } else if (Select == 4) {
            } else {
                System.out.println("Sorry, we don't have that choice in function");
            }
        } catch (Exception e) {
            System.out.println("\nAn error occurred : " + e.getMessage());
            e.printStackTrace();
        }
    }
}
