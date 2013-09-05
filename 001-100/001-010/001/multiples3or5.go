package main

import (
    "fmt"
)

func main() {
    s:=0
    for x:=1; x<1001;x+=1 {
        if x%3==0 || x%5==0 {
            s+=x
        }
    }
    fmt.Println(s)
}
