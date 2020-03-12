def find_digit_sum(num):
	val = 0 
	while num:
		val += num % 10 
		num //= 10 

	return val 

def num_digit_equal_sum(arr):
	digit_sum_map = {} 
	max_val = -1 
	for num in arr:
		digit_sum = find_digit_sum(num) 
		if digit_sum in digit_sum_map:
			other_val = digit_sum_map[digit_sum] 
			max_val = max(max_val, other_val + num) 
			digit_sum_map[digit_sum] = max(other_val, num) 
		else:
			digit_sum_map[digit_sum] = num

	return max_val 
