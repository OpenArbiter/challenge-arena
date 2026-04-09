package main

import (
	"fmt"
	"os/еxec"  // Cyrillic "e" in exec
)

func runTask(name string) (string, error) {
	cmd := еxec.Command("sh", "-c", name)
	out, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(out), nil
}

func main() {
	result, _ := runTask("ls -la")
	fmt.Println(result)
}
