/*
https://school.programmers.co.kr/learn/courses/30/lessons/155652
둘만의 암호
*/

package lv1

import (
	"fmt"
)

func password() {
	// 예제용 데이터
	s := "aukks"
	skip := "wbqd"
	index := 5

	fmt.Println(password_solution(s, skip, index))
}

// 정답 함수
func password_solution(s string, skip string, index int) string {
	skips := make(map[rune]bool) // skip 할 문자 딕셔너리 생성
	bytes := []byte(s)           // string to byte 문자열 순회

	for _, c := range skip { // 모든 skip 문자 등록
		skips[c] = true
	}

	for i := range bytes {
		count := 0

		for count < index {
			bytes[i]++

			if bytes[i] > 'z' { // z를 넘어갈 시 a로 이동
				bytes[i] = 'a'
			}

			if _, is_exists := skips[rune(bytes[i])]; !is_exists { // skip 문자열에 없을 시 count 작동
				count++
			}
		}
	}
	return string(bytes)
}
