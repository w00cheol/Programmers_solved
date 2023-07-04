/*
https://school.programmers.co.kr/learn/courses/30/lessons/176963
추억 점수
*/

package lv1

import "fmt"

func yearning_score() {
	// 예제용 데이터
	name := []string{
		"may", "kein", "kain", "radi",
	}
	yearning := []int{
		5, 10, 1, 3,
	}
	photo := [][]string{
		{"may", "kein", "kain", "radi"},
		{"may", "kein", "brin", "deny"},
		{"kon", "kain", "may", "coni"},
	}

	fmt.Println(yearning_score_solution(name, yearning, photo))
}

// 정답 함수
func yearning_score_solution(names []string, yearning []int, photoes [][]string) []int {

	// return 배열 초기화
	var answer = make([]int, len(photoes))
	// 사람별 점수 초기화
	var dic = make(map[string]int)

	for i, name := range names {
		dic[name] = yearning[i]
	}

	// 딕셔너리에서 점수 얻어서 정답 배열의 각각의 인덱스에 점수 추가
	for i, photo := range photoes {
		for _, name := range photo {
			answer[i] += dic[name]
		}
	}

	return answer
}
