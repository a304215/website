package main
import (
	"fmt"
	"time"
)
func f(x int){
	for i:=0;i<x;i++{
		fmt.Println(i)
	}
}
func main(){
	go f(10)
	time.Sleep(time.Second * 1)
	fmt.Println("it is finish")
}