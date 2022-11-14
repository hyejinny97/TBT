// ----- 분류 필터 -----
// 현재 필터에 따라 해당 dropdown-item에만 active 붙이기
const filter = document.querySelector('.pdt-filter').dataset.filter
const dropdownItems = document.querySelectorAll('.dropdown-item')
const filterType = {
  'register': 0,
  'high-sale': 1,
  'high-price': 2,
  'low-price': 3,
}

for (i = 0; i < dropdownItems.length; i++) {
  dropdownItems[i].classList.remove('active')
}

const idx = filterType[filter]
dropdownItems[idx].classList.add('active')

// 현재 active한 필터의 text를 버튼 text와 동일하게 설정
const dropdownBtn = document.querySelector('.dropdown-toggle')
const activeDropdownItem = document.querySelector('.dropdown-item.active')

dropdownBtn.innerText = activeDropdownItem.innerText