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
const body = document.querySelector('body');

try {

    revBtnOpenModal.addEventListener('click', function (e) {
        e.preventDefault();
        revModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');
    });
    qnaBtnOpenModal.addEventListener('click', function () {
        qnaModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');
    });
    revBtnCloseModal.addEventListener('click', function () {
        revModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    });
    qnaBtnCloseModal.addEventListener('click', function () {
        qnaModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    });
    // overlay.addEventListener('click', function () {
    //     body.classList.remove('scroll-block');
    //     revModal.classList.add('hidden');
    //     qnaModal.classList.add('hidden');
    //     overlay.classList.add('hidden');
    // })


    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            body.classList.remove('scroll-block');
            revModal.classList.add('hidden');
            qnaModal.classList.add('hidden');
            overlay.classList.add('hidden')
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

} catch {

}

try {
    const slider = function () {
        const slides = document.querySelectorAll('.slide');
        const btnLeft = document.querySelector('.slider-btn-left');
        const btnRight = document.querySelector('.slider-btn-right');
        const dotContainer = document.querySelector('.dots');

        let curSlide = 0;
        const maxSlide = slides.length;

        const createDots = function () {
            slides.forEach(function (_, i) {
                dotContainer.insertAdjacentHTML('beforeend', `<button class="dots-dot" data-slide="${i}"></button>`);
            })
        };
        const activeDot = function (slide) {
            document.querySelectorAll('.dots-dot').forEach(dot => dot.classList.remove('dots-dot-active'));
            document.querySelector(`.dots-dot[data-slide="${slide}"]`).classList.add('dots-dot-active');
        };

        const goToSlide = function (slide) {
            slides.forEach((s, i) => s.style.transform = `translateX(${100 * (i - slide)}%)`);
        }

        const nextSlide = function () {
            if (curSlide === maxSlide - 1) {
                curSlide = 0;
            } else {
                curSlide++;
            }

            goToSlide(curSlide);
            activeDot(curSlide);
        };

        const prevSlide = function () {
            if (curSlide === 0) {
                curSlide = maxSlide - 1;
            } else {
                curSlide--;
            }

            goToSlide(curSlide);
            activeDot(curSlide);
        };
        const init = function () {
            createDots();
            goToSlide(0);
            activeDot(0);
        };

        init();

        btnLeft.addEventListener('click', prevSlide);
        btnRight.addEventListener('click', nextSlide);

        document.addEventListener('keydown', function (e) {
            if (e.key === "ArrowLeft") prevSlide();
            e.key === "ArrowRight" && nextSlide();
        });

        dotContainer.addEventListener('click', function (e) {
            if (e.target.classList.contains('dots-dot')) {
                const { slide } = e.target.dataset;
                goToSlide(slide);
                activeDot(slide);
            }
        });
        setInterval(nextSlide, 6000);
    };

    slider();
} catch {

}

try {

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

} catch {

}


const likeBtn = document.querySelectorAll(".like-btn");
try {

    const reviewlike = function (event) {
        // console.log(event.target.closest('.like-btn'));
        const reviewId = event.target.dataset.reviewId
        axios({
            method: 'get',
            url: `/reviews/${reviewId}/likes/`
        })
            .then((response) => {
                const isLiked = response.data.isLiked;
                if (isLiked === true) {
                    event.target.classList.add('bi-hand-thumbs-up-fill');
                    event.target.classList.remove('bi-hand-thumbs-up');
                    event.target.closest('.like-btn').classList.add('like-active');
                } else {
                    event.target.classList.add('bi-hand-thumbs-up');
                    event.target.classList.remove('bi-hand-thumbs-up-fill');
                    event.target.closest('.like-btn').classList.remove('like-active');

                }

                const likeCount = event.target.nextElementSibling;
                likeCount.innerText = response.data.likeCount;
            })
    }

    likeBtn.forEach(btn => {
        btn.addEventListener('click', reviewlike);
    })
} catch {

}
