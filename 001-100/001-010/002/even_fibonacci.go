package main

import (
    "fmt"
)

func main() {
    a:=1
    b:=1
    s:=0
    for {
        if b>=4000000 {
            break
        }
        a=b
        b+=a
        if a%2==0 {
            s+=a
        }
    }

    fmt.Println(s)
}
