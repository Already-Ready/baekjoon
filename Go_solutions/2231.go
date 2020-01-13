package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	if n == 1 {
		fmt.Printf("%d", 0)
	}

	for i := 1; i < n; i++ {
		sum := i
		for _, j := range strconv.Itoa(sum) {
			k, _ := strconv.ParseInt(string(j), 10, 8)
			sum += int(k)
		}
		if sum == n {
			fmt.Printf("%d", i)
			break
		} else if i == n-1 {
			fmt.Printf("%d", 0)
		}
	}
}
