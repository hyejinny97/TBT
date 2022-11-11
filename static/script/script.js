'use strict';

const form = document.querySelector('#follow-form');

const revModal = document.querySelector('#review');
const qnaModal = document.querySelector('#qna');
const overlay = document.querySelector('.overlayC');
const revBtnCloseModal = document.querySelector('.btn-close-rev');
const qnaBtnCloseModal = document.querySelector('.btn-close-qna');
const revBtnOpenModal = document.querySelector('#rev-modal-btn');
const qnaBtnOpenModal = document.querySelector('.qna-modal-btn');
const detailArea = document.querySelector('#product-detail');



revBtnOpenModal.addEventListener('click', function (e) {
    e.preventDefault();
    revModal.classList.remove('hidden');
    overlay.classList.remove('hidden');
    detailArea.classList.add('scroll-block');
});
qnaBtnOpenModal.addEventListener('click', function () {
    qnaModal.classList.remove('hidden');
    overlay.classList.remove('hidden');
    detailArea.classList.add('scroll-block');
});
revBtnCloseModal.addEventListener('click', function () {
    revModal.classList.add('hidden');
    overlay.classList.add('hidden');
    detailArea.classList.remove('scroll-block');
});
qnaBtnCloseModal.addEventListener('click', function () {
    qnaModal.classList.add('hidden');
    overlay.classList.add('hidden');
    detailArea.classList.remove('scroll-block');
});


document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
    }
});

const tabCont = document.querySelector('.cate-area');
const tabs = document.querySelectorAll('.tab_oper');

tabCont.addEventListener('click', function (e) {
    const clicked = e.target.closest('.tab_oper');
    if (!clicked) return;
    tabs.forEach(t => t.classList.remove('tab-active'));
    clicked.classList.add('tab-active');
});


form.addEventListener('submit', function (e) {
    e.preventDefault();
    const userId = e.target.dataset.userId;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    axios({
        method: 'POST',
        url: `/accounts/${userId}/follow/`,
        headers: { 'X-CSRFToken': csrftoken, }
    })
        .then(response => {
            console.log(response.data.isFollow);
            const isFollow = response.data.isFollow;
            const followBtn = document.querySelector('#follow-btn');
            if (isFollow === true) {
                followBtn.innerText = 'unfollow'
                followBtn.classList.remove('follow__btn');
                followBtn.classList.add('unfollow__btn');
            } else {
                followBtn.innerText = 'follow'
                followBtn.classList.remove('unfollow__btn');
                followBtn.classList.add('follow__btn');

            }
            const followersCount = document.querySelector('#followers-count');
            const followingsCount = document.querySelector('#followings-count');
            const followersCountValue = response.data.followers_count;
            const followingsCountValue = response.data.followings_count;
            followersCount.innerText = followersCountValue;
            followingsCount.innerText = followingsCountValue;
        })
});


