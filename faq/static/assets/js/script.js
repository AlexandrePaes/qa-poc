// static/assets/js/script.js

document.getElementById('submit-btn').addEventListener('click', function () {
    var nextPage = parseInt(document.getElementById('question-id-input').value) + 1;
    window.location.href = window.location.pathname
    window.location.href = window.location.href + '?page=question-id-input'
    window.location.href + nextPage;
  });
  