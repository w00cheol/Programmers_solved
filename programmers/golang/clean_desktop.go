/*
https://school.programmers.co.kr/learn/courses/30/lessons/161990
바탕화면 정리
*/

package lv1

import (
	"fmt"
	"math"
)

func clean_desktop() {
	// 예제용 데이터
	wallpaper := []string{
		".#...", "..#..", "...#.",
	}

	fmt.Println(clean_desktop_solution(wallpaper))
}

// 정답 함수
func clean_desktop_solution(wallpaper []string) []int {
	l, r, u, d := float64(len(wallpaper[0])), 0.0, float64(len(wallpaper)), 0.0
	for x, width := range wallpaper {
		for y := range width {
			if wallpaper[x][y] == '#' {
				l = math.Min(float64(l), float64(y)) // 최좌측 인덱스 변경
				r = math.Max(float64(r), float64(y)) // 최우측 인덱스 변경
				u = math.Min(float64(u), float64(x)) // 최상단 인덱스 변경
				d = math.Max(float64(d), float64(x)) // 최하단 인덱스 변경
			}
		}
	}

	return []int{int(u), int(l), int(d + 1), int(r + 1)} // 우측과 하단은 1만큼의 인덱스가 증가되어야함 (인덱스가 덮어져야하기 때문)
}
