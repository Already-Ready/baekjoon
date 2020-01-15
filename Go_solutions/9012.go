package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func vps(x string) string {
	var stack []string

	for idx, ch := range x {
		s := string(ch)
		if idx == 0 && s == ")" {
			return "NO"
		} else {
			if s == "(" {
				stack = append(stack, s)
			} else if s == ")" && stack != nil {
				length := len(stack)
				if length == 1 {
					stack = nil
				} else {
					stack = stack[:length-1]
				}
			} else {
				return "NO"
			}
		}
	}
	if stack == nil {
		return "YES"
	} else {
		return "NO"
	}
}

func main() {
	var n int
	inputReader := bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		input, _ := inputReader.ReadString('\n')
		action := strings.TrimSpace(input)

		answer := vps(action)

		fmt.Println(answer)
	}
}
