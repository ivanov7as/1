class Solution {
    public String SimplifyPath(String path) {
            String[] parts = path.split("/");
            Stack<String> stack = new Stack<String>();
            for (String part : parts) {
                if (part.isEmpty() || part.equals(".")) continue;
                if (part.equals("..")) {
                    if (!stack.isEmpty())
                        stack.pop();
                } else {
                    stack.push(part);
                }
            }
            return "/" + String.join("/", stack);
        }
}
