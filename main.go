package main

import (
	"fmt"
	"io"
	"net/http"
)

const (
	WALLHAVEN_KEY    = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
	WALLHAVEN_TAG    = "https://wallhaven.cc/api/v1/tag/"
	WALLHAVEN_SEARCH = "https://wallhaven.cc/api/v1/search"
)

func wallhaven_tag_info(id string) string {
	return WALLHAVEN_TAG + id
}

func wallhaven_tag_page(id string) string {
	return WALLHAVEN_SEARCH + "?apikey=" + WALLHAVEN_KEY + "&q=id:" + id + "&page="
}

func wallhaven_json(url string) []byte {
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	// TODO: return json
	return body
}

func main() {
	id := "120"

	fmt.Printf("%s\n", wallhaven_json(wallhaven_tag_info(id)))

	fmt.Printf("%s\n", wallhaven_json(wallhaven_tag_page(id)+"1"))
}
