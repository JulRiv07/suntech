(function(){
    const titledate = [...document.querySelectorAll('.date_title')];
    console.log(titledate)

    titledate.forEach(question =>{
        question.addEventListener('click', ()=>{
            let height = 0;
            let answer = question.nextElementSibling;
            let addPadding = question.parentElement.parentElement;

            addPadding.classList.toggle('date_padding--add');
            question.children[0].classList.toggle('date_arrow--rotate');

            if(answer.clientHeight === 0){
                height = answer.scrollHeight;
            }

            answer.style.height = `${height}px`;
        });
    });
})();