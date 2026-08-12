"""
This is a stack problem.

We create a stack that scans each character of the path given.
By remembering the previous characters, and following the rules of the
Unix-style file system, we only append what we deem to be part of the 
simplified canonical path.

O(n) time complexity
with O(n) space complexity 


RULES:

1. Multiple consecutive slashes are treated as a single slash. / cannot be part of the path name
2. A single dot, refers to the current directory, and should not be included
3. A double dot, refers to a directoy previous, and therefore should remove the current directory of the path
4. A triple dot or more, should simply just be a directory name
5. Path must start with '/'
6. Path no end with '/' unless its total length is 1

    

"""



class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0

        while i < len(path):
            if path[i] == "/": #Rule 1
                while i < len(path) and path[i] == "/":
                    i += 1
                if not stack:
                    stack.append("/")
                elif stack[-1] != "/":
                    stack.append("/")
            elif path[i] == ".":
                count = 0
                while i < len(path) and path[i] == ".":
                    count += 1
                    i += 1
                if count > 2 or (i < len(path) and path[i] != "/"):
                    stack.append("." * count)
                elif count == 2:
                    stack.pop() #remove the /
                    #Remove current directory logic
                    while stack and stack[-1] != "/":
                        stack.pop()
                elif stack and stack[-1] != "/":
                    stack.append(".")


                    
            else:
                stack.append(path[i])
                i += 1

        if len(stack) != 1 and stack[-1] == "/":
            stack.pop()
        
        canon_path = "".join(stack)
        return canon_path
        


"""
Problems:

We have to include the dot within the character, but if it just a dot by itself, then don't include it.

"""
            
            
            

