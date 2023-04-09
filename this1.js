
const form = document.querySelector("form");
const input = document.querySelector('input');
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const fs = require("fs");

    const usercomment = require("./usercomment.json");
    const comments = usercomment[input.value];

    const commentList = document.getElementById("comment-list");

    comments.forEach(comment => {
        const li = document.createElement("li");
        li.textContent = comment.comment;
        commentList.appendChild(li);
    });
})