'use strict';


const form = document.querySelector('#follow-form');

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
