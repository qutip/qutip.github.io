$(document).ready(function(){
    $('.education-carousel').slick({
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2500,
        infinite: true,
        dots: true,
        arrows: false,
        mobileFirst: true,
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 4,
                    centerMode: false,
                }
            },
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    centerMode: true,
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    centerMode: true,
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 576,
                settings: {
                    centerMode: true,
                    slidesToShow: 1,
                }
            }
        ],
    });
});