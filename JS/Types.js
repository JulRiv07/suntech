(() => {
    const viewport = document.querySelector('.types_viewport');
    const track = document.querySelector('.types_track');
    const cards = Array.from(track.children);
    const prev = document.querySelector('.types_prev');
    const next = document.querySelector('.types_next');

    if (!viewport || !track || cards.length === 0) {
        return;
    }

    let index = 0;

    function cardWidth(){
        return viewport.clientWidth + 24;
    }

    function update(){
        const x = -index * cardWidth();
        track.style.transform = `translateX(${x}px)`;
        prev.disabled = index === 0;
        next.disabled = index === cards.length - 1;
        [prev,next].forEach(btn => {
            btn.style.opacity = btn.disabled ? .35 : 1;
            btn.style.cursor  = btn.disabled ? 'default' : 'pointer';
        });
    }

    function nextSlide(){ 
        if (index < cards.length - 1){ 
            index++; update(); 
        } 
    }

    function prevSlide(){ 
        if (index > 0){ 
            index--; update(); 
        } 
    }

    next.addEventListener('click', nextSlide);
    prev.addEventListener('click', prevSlide);

    window.addEventListener('keydown', e => {
        if (window.innerWidth >= 992){
            if (e.key === 'ArrowRight'){ 
                nextSlide();
            } 
            if (e.key === 'ArrowLeft') {
                prevSlide();
            } 
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth >= 992) {
            update();
        } else track.style.transform = '';
    });

    update();
    
})();
