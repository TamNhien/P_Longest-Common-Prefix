def longestCommonPrefix(strs):
    # Nếu mảng rỗng, trả về chuỗi trống
    if not strs:
        return ""
    
    # Duyệt qua từng ký tự của chuỗi đầu tiên
    for i, char in enumerate(strs[0]):
        # Duyệt qua các chuỗi còn lại trong mảng
        for string in strs[1:]:
            # Nếu chuỗi không chứa ký tự tương ứng, trả về chuỗi tiền tố đến vị trí i
            if i > len(string) or string[i] != char:
                return strs[0][:i]
            
    # Nếu không có chuỗi nào trong mảng, trả về chuỗi đầu tiên
    return strs[0]

# Test
print(longestCommonPrefix(["flower","flow","flight"])) # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))    # Output: ""    