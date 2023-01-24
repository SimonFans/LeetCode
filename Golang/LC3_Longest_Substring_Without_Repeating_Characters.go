func lengthOfLongestSubstring(s string) int {
    longest := 0
    visited := make(map[byte]int)
    start := 0 
    for i:=0; i < len(s); i++{
        c:= s[i]
        // 1. if already existed 2. current i >= start exp: "abba"
        if _, ok := visited[c];ok && visited[c] >= start {
            start = visited[c] + 1
        }
        // get the max length
        longest = max(longest, i - start +1)
        // record current char index
        visited[c] = i
    }
    return longest
}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}
