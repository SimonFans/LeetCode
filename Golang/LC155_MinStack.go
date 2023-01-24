type MinStack struct {
    nums []int
    minVal int
}


func Constructor() MinStack {
    return MinStack {
        nums: []int{},
        minVal: 1<<63-1,
    }
}


func (this *MinStack) Push(val int)  {
    this.nums = append(this.nums, val)
    if val < this.minVal{
        this.minVal = val
    }
}


func (this *MinStack) Pop()  {
    // take out the top element
    topElement := this.nums[len(this.nums)-1]
    // remove the top element
    this.nums = this.nums[:len(this.nums)-1]
    // recalculate the mini value
    if topElement == this.minVal && len(this.nums) > 0{
        newMini := this.nums[0]
        for _, num := range this.nums{
            if num < newMini{
                newMini = num
            }
        }
        this.minVal = newMini
    }
    // edge case if after top, there is no element then set the default miniVal
    if len(this.nums) == 0{
        this.minVal = 1 << 63 -  1 // 1 * 2^63 -1
    }
}


func (this *MinStack) Top() int {
    return this.nums[len(this.nums)-1]
}


func (this *MinStack) GetMin() int {
    return this.minVal
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
