package main

import (
	"crypto/aes"
	"encoding/hex"
	"fmt"
	"log"
)

func main() {
	hexFlag := "f90174665bb0505d9311282d72d62d62"
	key := "actually-maybe-dont-go-for-it-yo"
	fmt.Println(Decrypt([]byte(key), hexFlag))
}

func Decrypt(key []byte, ct string) string {
	ciphertext, _ := hex.DecodeString(ct)
	c, err := aes.NewCipher(key)
	if err != nil {
		log.Println("ruh roh")
	}
	pt := make([]byte, len(ciphertext))
	c.Decrypt(pt, ciphertext)
	return string(pt[:])
}
