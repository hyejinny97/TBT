// 별점 소수점으로 채우기
const starsColor = document.querySelector('.stars-color')

avgOfGrade = starsColor.dataset.avgGrade ? starsColor.dataset.avgGrade : 0
starsColor.style.width = `${avgOfGrade / 5 * 118}px`




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



