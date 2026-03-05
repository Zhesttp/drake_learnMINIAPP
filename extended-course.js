(function () {
    var blocks = document.querySelectorAll('.ext-course-block');
    blocks.forEach(function (block) {
        var head = block.querySelector('.ext-course-block-head');
        var body = block.querySelector('.ext-course-block-body');
        if (!head || !body) return;
        head.addEventListener('click', function () {
            var isOpen = head.getAttribute('aria-expanded') === 'true';
            head.setAttribute('aria-expanded', !isOpen);
            body.hidden = isOpen;
            block.classList.toggle('ext-course-block-open', !isOpen);
        });
    });
})();
