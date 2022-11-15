// 별점 소수점으로 채우기
const starsColorAll = document.querySelectorAll('.stars-color')

for (let starsColor of starsColorAll) {
  avgOfGrade = starsColor.dataset.avgGrade ? starsColor.dataset.avgGrade : 0
  starsColor.style.width = `${avgOfGrade / 5 * 118}px`
}



// 수량 버튼을 눌렀을 때 수량 증감 및 주문 금액 계산 
const minusBtn = document.querySelector('.minus-btn')
const plusBtn = document.querySelector('.plus-btn')
const buyMount = document.querySelector('.buy-mount')

const totalPurchasePrice = document.querySelector('.total-purchase-price')
const deliveryPrice = parseInt(totalPurchasePrice.dataset.delivery)
const pdtPrice = parseInt(totalPurchasePrice.dataset.price)
const sale = parseInt(totalPurchasePrice.dataset.sale)

const calTotPurchasePrice = function (mount) {   // 주문 금액 구하기
  if (mount !== 0) {
    totalPurchasePrice.innerText = `${(pdtPrice * (100 - sale) * 0.01 * mount + deliveryPrice).toLocaleString('ko-KR')}원`
  } else {
    totalPurchasePrice.innerText = '0원'
  }
}

plusBtn.addEventListener('click', function () {
  buyMount.innerText = parseInt(buyMount.innerText) + 1
  let mount = parseInt(buyMount.innerText)
  calTotPurchasePrice(mount)
})

minusBtn.addEventListener('click', function () {
  if (parseInt(buyMount.innerText) - 1 >= 0) {
    buyMount.innerText = parseInt(buyMount.innerText) - 1
  }
  let mount = parseInt(buyMount.innerText)
  calTotPurchasePrice(mount)
})



// 상품정보/리뷰/문의/추천 탭 클릭 시, 클래스에 active 추가
const tabs = document.querySelectorAll('.tab')

tabs.forEach(function (tab) {
  tab.addEventListener('click', function (event) {
    for (let tab of tabs) {
      tab.classList.remove('active')
    }
    event.currentTarget.classList.add('active')
    console(event.currentTarget)
  })
})



// 각 리뷰의 평점 갯수에 따라 grade-bar 채우기
const gradeBarColorAll = document.querySelectorAll('.grade-bar-color-wrap')
const gradeCounts = document.querySelectorAll('.pdt-review-grade-count')

let totCounts = 0
for (let gradeCount of gradeCounts) {
  totCounts += parseInt(gradeCount.innerText)
}

for (i = 0; i < 5; i++) {
  gradeBarColorAll[i].style.width = `${160 * parseInt(gradeCounts[i].innerText) / totCounts}px`
}

// for (let starsColor of gradeBarColorAll) {
//   avgOfGrade = starsColor.dataset.avgGrade ? starsColor.dataset.avgGrade : 0
//   starsColor.style.width = `${avgOfGrade / 5 * 118}px`
// }