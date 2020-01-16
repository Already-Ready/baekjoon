package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	count := 0
	name := 666
	fmt.Scanf("%d", &n)

	for {
		if count == n {
			fmt.Printf("%d", name-1)
			break
		} else {
			check := 0
			for _, k := range strconv.Itoa(name) {
				v, _ := strconv.ParseInt(string(k), 10, 8)
				if v == 6 {
					check += 1
					switch check {
					case 3:
						count += 1
					}
				} else {
					check = 0
				}
			}
		}
		name += 1
	}
}
