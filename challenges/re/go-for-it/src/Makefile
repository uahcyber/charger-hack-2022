all:
	GOOS=linux GOARCH=amd64 go build -ldflags "-w" -o ../to_copy/go-for-it main.go
	cp ../to_copy/go-for-it ../dist/go-for-it
clean:
	-rm ../to_copy/go-for-it ../dist/go-for-it