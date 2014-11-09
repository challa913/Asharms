/**
 * jQuery for home.html
 */
$(document).ready(function() {
    document.getElementById("hide-all").style.display = "none";
    imgSlide();
});
$(window).load(function(){
    childCountAnimate(100);
    ashramCountAnimate(10);
});
function imgSlide(){
     $('#slides').slidesjs({
            play: {
                effect: "fade",
                active: true,
                auto: true,
                interval: 4000,
                swap: true
            },
            navigation: {
                effect: "fade"
            },
            pagination: {
                effect: "fade"
            },
            effect: {
                fade: {
                    speed: 400
                }
            }

        });
}
function childCountAnimate(count) {
     $('#child-count')
            .prop('number', 0)
            .animateNumber(
            {
                number: count
            },
            2000
        );
}
function ashramCountAnimate(count){
     $('#ashram-count')
            .prop('number', 0)
            .animateNumber(
            {
                number: count
            },
            2000
        );
}
