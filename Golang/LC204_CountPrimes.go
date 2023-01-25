func countPrimes(n int) int {
    count := 0
    if n < 2{
        return count
    }
    flag := make([]bool,n)
    for i:=0; i<n; i++{
        flag[i] = true
    }
    flag[0], flag[1] = false, false
    i := 2
    for i*i < n {
        for j := i*i; j < n; j += i{
            flag[j] = false
        }
        i += 1
    }
    for i := 0; i < len(flag); i++ {
        if flag[i] == true {
            count += 1
        }
    }
    return count
}
