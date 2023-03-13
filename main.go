package main

import (
	"fmt"
)

const (
	WALLHAVEN_KEY    = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
	WALLHAVEN_TAG    = "https://wallhaven.cc/api/v1/tag/"
	WALLHAVEN_SEARCH = "https://wallhaven.cc/api/v1/search"
)

func main() {
	id := "37"
	fmt.Println(wallhaven_tag_page(id))
}

func wallhaven_tag_page(s string) string {
	return WALLHAVEN_SEARCH + "?apikey=" + WALLHAVEN_KEY + "&q=id:" + s + "&page="
}
