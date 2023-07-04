/*
https://school.programmers.co.kr/learn/courses/30/lessons/147355
크기가 작은 부분문자열
*/

package lv1

import (
	"fmt"
)

func substring() {
	// 예제용 데이터
	t := "3141592"
	p := "271"

	fmt.Println(substring_solution(t, p))
}

// 정답 함수
func substring_solution(t string, p string) int {
	answer := 0

	// 문자열 순회를 위한 형변환
	b_t, b_p := []byte(t), []byte(p)

	// len(p)길이의 substring 모든 경우의 수 검색
	for i := 0; i < len(t)-len(p)+1; i++ {
		var flag bool = true

		for runner := 0; runner < len(p); runner++ {
			a := b_t[i+runner]
			b := b_p[runner]

			if a < b { // 앞자리가 작다면 즉시 정답처리 for문 탈출
				flag = true
				break
			} else if a > b { // 앞자리가 크면 오답처리 for문 탈출
				flag = false
				break
			}
			// 숫자가 같을 경우 다음 인덱스 확인
		}

		if flag {
			answer++
		}
	}
	return answer
}
