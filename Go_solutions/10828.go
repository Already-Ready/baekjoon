package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var s []int

func s_push(x int) {
	s = append(s, x)
}

func s_pop() {

	if s == nil {
		fmt.Printf("%d\n", -1)
	} else if len(s) == 1 {
		top := s[0]
		fmt.Printf("%d\n", top)
		s = nil
	} else {
		l := len(s)
		top := s[l-1]
		fmt.Printf("%d\n", top)
		s = s[:l-1]
	}
}

func s_size() {
	l := len(s)
	fmt.Printf("%d\n", l)
}

func s_empty() {
	if s == nil {
		fmt.Printf("%d\n", 1)
	} else {
		fmt.Printf("%d\n", 0)
	}
}

func s_top() {
	if s == nil {
		fmt.Printf("%d\n", -1)
	} else {
		l := len(s)
		top := s[l-1]
		fmt.Printf("%d\n", top)
	}
}

func main() {
	var n int
	inputReader := bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &n)

	for i := 0; i < n+1; i++ {
		input, _ := inputReader.ReadString('\n')

		order := strings.Split(input, " ")

		action := strings.TrimSpace(order[0])

		if len(order) == 2 {
			n := strings.TrimSpace(order[1])
			num, _ := strconv.Atoi(n)
			s_push(num)
		} else {
			switch action {
			case "pop":
				s_pop()
			case "size":
				s_size()
			case "empty":
				s_empty()
			case "top":
				s_top()
			}
		}
	}

	// inputReader := bufio.NewReader(os.Stdin)
	// input, _ := inputReader.ReadString('\n')
	// order := strings.Split(input, " ")
	// fmt.Println(len(order))
	// fmt.Println(order[0])
	// n := strings.TrimSpace(order[1])
	// fmt.Printf("%s", n)
	// fmt.Printf("%T\n", n)
	// num, _ := strconv.Atoi(n)
	// fmt.Printf("%T\n", num)
	// fmt.Printf("%d", num)

	// k := len(s)
	// fmt.Printf("%d", k)
	// s = append(s, 1)
	// s = append(s, 2)
	// l := len(s)
	// fmt.Println(s[:l])
	// fmt.Printf("%d", 1)
}
