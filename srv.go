package main

import (
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"strings"
)

func contains(s []string, e string) bool {
	for _, a := range s {
		if strings.Contains(e, a) {
			return true
		}
	}
	return false
}

func cleanOutput(cmd []byte) []byte {
	t := strings.Split(string(cmd), "\n")[1:]
	str := ""
	for _, v := range t {
		str += strings.Join(strings.Split(v, "\t")[1:], "\t") + " "
	}
	return []byte(str)
}

func handl(w http.ResponseWriter, r *http.Request) {
	message := r.URL.Path

	abbr := []string{"1 Mos", "2 Mos", "3 Mos", "4 Mos", "5 Mos", "Jos", "Dom", "Rut", "1 Sam", "2 Sam", "1 Kung", "2 Kung", "1 Krön", "2 Krön", "Esr", "Neh", "Est", "Job", "Ps", "Ords", "Pred", "Höga v", "Jes", "Jer", "Klag", "Hes", "Dan", "Hos", "Joel", "Am", "Ob", "Jon", "Mik", "Nah", "Hab", "Sef", "Hagg", "Sak", "Mal", "Matt", "Mark", "Luk", "Joh", "Apg", "Rom", "1 Kor", "2 Kor", "Gal", "Ef", "Fil", "Kol", "1 Thess", "2 Thess", "1 Tim", "2 Tim", "Tit", "Filem", "Heb", "Jak", "1 Pet", "2 Pet", "1 Joh", "2 Joh", "3 Joh", "Jud", "Upp"}

	message = strings.TrimPrefix(message, "/")

	if contains(abbr, message) {
		cmd, err := exec.Command("./sfb98", "-W", message).Output()
		if err != nil || strings.Contains(string(cmd), "Unknown reference:") {
			fmt.Println(err)
			w.WriteHeader(401)
			w.Write([]byte("Error: The requested passage does not exist\n"))
			w.Write(cmd)
			return
		}

		_, ok := r.URL.Query()["annotate"]
		if !ok {
			cmd = cleanOutput(cmd)
		}

		w.WriteHeader(200)
		w.Write(cmd)

		return
	}

	if r.URL.Path == "" || r.URL.Path == "/" {
		http.ServeFile(w, r, "index.html")
		return
	}
	http.ServeFile(w, r, message)
}

func main() {
	http.HandleFunc("/", handl)
	if len(os.Args) == 1 {
		fmt.Println("ERR: Supply a port")
		os.Exit(1)
	}
	port := ":" + string(os.Args[1])
	fmt.Println("Listening on " + port)
	if err := http.ListenAndServe(port, nil); err != nil {
		panic(err)
	}
}
