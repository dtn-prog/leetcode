package main

import (
	"fmt"
)

func longestConsecutive(nums []int) int {
	numsMap := make(map[int]struct{})
	// create the hash map
	for _, val := range nums {
		numsMap[val] = struct{}{}
	}
	size := len(nums)
	fmt.Println(numsMap)
	sequenceStarts := make([]int, 0, size)

	//get the starting number of sequence
	for k := range numsMap {
		left := k - 1
		_, exists := numsMap[left]
		if !exists {
			sequenceStarts = append(sequenceStarts, k)
		}
	}

	fmt.Println(sequenceStarts)
	result := 0
	for _, val := range sequenceStarts {
		i := 1
		for {
			_, exists := numsMap[val+1]
			if exists {
				val++
				i++
			} else {
				break
			}
		}

		if result < i {
			result = i
		}

	}

	return result
}

func main() {
	nums := []int{100, 4, 200, 1, 3, 2}
	fmt.Println(longestConsecutive(nums))
}
