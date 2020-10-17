const group_btn = document.getElementById('group-btn')
const post_btn = document.getElementById('post-btn')
const user_btn = document.getElementById('user-btn')
const group_list = document.getElementById('group-list')
const post_list = document.getElementById('post-list')
const user_list = document.getElementById('user-list')

console.log(group_list)

group_list.style.visibility = "visible";
post_list.style.visibility = "hidden";
user_list.style.visibility = "hidden";

group_btn.addEventListener('click', e => {
    group_list.style.visibility = "visible";
    post_list.style.visibility = "hidden";
    user_list.style.visibility = "hidden";
})

post_btn.addEventListener('click', e => {
    group_list.style.visibility = "hidden";
    post_list.style.visibility = "visible";
    user_list.style.visibility = "hidden";
})

user_btn.addEventListener('click', e => {
    group_list.style.visibility = "hidden";
    post_list.style.visibility = "hidden";
    user_list.style.visibility = "visible";
})