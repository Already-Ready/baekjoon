package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func vps(x string) string {
	var stack []string

	// fmt.Println(string(x[0]))
	// return x
	if string(x[0]) == ")" || string(x[0]) == "]" {
		return "no"
	}
	for _, ch := range x {
		s := string(ch)
		match, _ := regexp.MatchString("[a-zA-Z]", s)
		if match == true {
		} else if s == " " || s == "." {
		} else if s == "(" || s == "[" {
			stack = append(stack, s)
		} else if s == ")" && stack != nil {
			if stack[len(stack)-1] == "(" {
				if len(stack) == 1 {
					stack = nil
				} else {
					stack = stack[:len(stack)-1]
				}
			} else {
				return "no"
			}
		} else if s == "]" && stack != nil {
			if stack[len(stack)-1] == "[" {
				if len(stack) == 1 {
					stack = nil
				} else {
					stack = stack[:len(stack)-1]
				}
			} else {
				return "no"
			}
		} else {
			return "no"
		}
	}
	if stack == nil {
		return "yes"
	} else {
		return "no"
	}
}

func main() {
	inputReader := bufio.NewReader(os.Stdin)
	var story []string
	for {
		input, _ := inputReader.ReadString('\n')
		action := strings.TrimSpace(input)
		// fmt.Printf("%d\n", len(input))
		story = append(story, action)

		// fmt.Println(story)

		if string(input[0]) != " " && strings.TrimSpace(input) == "." {
			break
		}
		// fmt.Println(story)
	}
	// fmt.Println(story)
	for _, line := range story[:len(story)-1] {
		answer := vps(line)
		fmt.Println(answer)
	}
}
