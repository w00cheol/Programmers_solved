/*
https://school.programmers.co.kr/learn/courses/30/lessons/161989
덧칠하기
*/

package lv1

import (
	"fmt"
)

func paint() {
	// 예제용 데이터
	n, m := 8, 4
	section := []int{
		2, 3, 6,
	}

	fmt.Println(paint_solution(n, m, section))
}

// 정답 함수
func paint_solution(n int, m int, section []int) int {
	answer, painted := 0, 0
	for _, num := range section {
		if num > painted { // n이 포함되지 않았다면 횟수 1 추가 후 최대반경 업데이트
			painted = num + m - 1
			answer++
		}
	}
	return answer
}
