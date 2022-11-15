// 별점 소수점으로 채우기
const starsColor = document.querySelector('.stars-color')

avgOfGrade = starsColor.dataset.avgGrade ? starsColor.dataset.avgGrade : 0
starsColor.style.width = `${avgOfGrade / 5 * 118}px`