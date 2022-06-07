package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := ""
	matched, err := regexp.MatchString("^[0-9]*$", str)
	fmt.Println(matched, err)
}
