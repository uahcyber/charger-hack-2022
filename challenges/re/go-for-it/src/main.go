package main

import (
	"crypto/aes"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	fileContent, err := ioutil.ReadFile("flag.txt")
	if err != nil {
		log.Fatal(err)
	}
	flag := string(fileContent)
	key := "actually-maybe-don"
	key += "t-go-for-it-yo"
	fmt.Println(Encrypt([]byte(key), flag))
}

func Encrypt(key []byte, text string) string {
	c, err := aes.NewCipher(key)
	if err != nil {
		log.Fatal("ruh roh")
	}
	out := make([]byte, len(text))
	c.Encrypt(out, []byte(text))
	return hex.EncodeToString(out)
}
