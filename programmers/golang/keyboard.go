/*
https://school.programmers.co.kr/learn/courses/30/lessons/160586
대충 만든 자판
*/

package lv1

import (
	"fmt"
	"math"
)

func keyboard() {
	// 예제용 데이터
	keymap := []string{
		"ABACD", "BCEFD",
	}
	targets := []string{
		"ABCD", "AABB",
	}

	fmt.Println(keyboard_solution(keymap, targets))
}

// 정답 함수
func keyboard_solution(keymap []string, targets []string) []int {
	answer := make([]int, len(targets))
	min_count := make(map[rune]int) // 가장 낮은 수를 지정할 키맵 초기화

	for _, chs := range keymap { // 모든 키맵 순회
		for i, ch := range chs { // 각 키맵의 모든 문자 순회
			if _, is_exists := min_count[ch]; is_exists { // 문자 별 최솟값으로 업데이트
				min_count[ch] = int(math.Min(float64(min_count[ch]), float64(i)))
			} else {
				min_count[ch] = i
			}
		}
	}

	for i, target := range targets {
		sum := 0
		for _, ch := range target {
			if _, is_exists := min_count[ch]; is_exists { // keymap 의 각 key 에 접근하여 가장 낮은 수 합산
				sum += min_count[ch] + 1 // 첫 인덱스가 0이기 때문에 1 추가
			} else { // 만약 map 에 키가 없는것이 있다면 result = -1
				sum = -1
				break
			}
		}
		answer[i] = sum
	}

	return answer
}
