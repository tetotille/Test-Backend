# Code Challenges
def balancedGroupSymbols(data:str) -> bool:
    """
        This function receive a string and return True or False depending of the
        symbols are consistents.
        O(n) complex

        Input:
            data (str): String to be verify

        Output:
            (bool) True or False
    """
    stack = []
    for symbol in data:
        if symbol == "(" or symbol == "[" or symbol == "{":
            stack.append(symbol)
        else:
            previous_symbol = stack.pop()
            if previous_symbol != "(" and symbol == ")": return False
            elif previous_symbol != "[" and symbol == "]": return False
            elif previous_symbol != "{" and symbol == "}": return False
    return True

def snail(matrix:list[list]) -> list:
    x = len(matrix)
    if x == 0: return None
    y = len(matrix[0])

    if x != y:
        print("Error: this is not an nxn array.")
        exit()
    
    # Set the limits
    left_limit = 0; right_limit = x; top_limit = 0; bottom_limit = y
    
    result = []

    selector = 0
    while x > 0 and y > 0:
        # Right direction
        if selector == 0:
            for j in range(left_limit, right_limit, 1):
                result.append(matrix[top_limit][j])
                
            y -= 1
            top_limit += 1
            selector = 1
            continue
        
        # Down direction
        if selector == 1:
            for i in range(top_limit, bottom_limit, 1):
                result.append(matrix[i][right_limit-1])
                
            x -= 1
            right_limit -= 1
            selector = 2
            continue

        # Left direction
        if selector == 2:
            for j in range(right_limit-1, left_limit-1, -1):
                result.append(matrix[bottom_limit-1][j])
                
            y -= 1
            bottom_limit -= 1
            selector = 3
            continue

        # Up direction
        if selector == 3:
            for i in range(bottom_limit-1, top_limit-1, -1):
                result.append(matrix[i][left_limit])
                
            left_limit += 1
            x -= 1

            selector = 0
            continue
    return result

if __name__ == "__main__":
    expression = "[()]{}{()()}"
    print(balancedGroupSymbols(expression))
    other_expression = "[(])"
    print(balancedGroupSymbols(other_expression))

    test_array = [  [1, 2,  3,  4],
                    [5, 6,  7,  8],
                    [9, 10, 11, 12],
                    [13,14, 15, 16]]
    print(snail(test_array))
