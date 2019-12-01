"use strict"; // Start of use strict



//Contact Form Validation



function CounterNumberChanger () {

    var timer = $('.timer');

    if(timer.length) {

        timer.appear(function () {

            timer.countTo();

        })

    }



}

// add your custom functions 

function serviceCarosule () {

    if ($('#services .owl-carousel').length) {

        $('#services .owl-carousel').owlCarousel({

            loop: true,

            nav: true,

            dots: false,

            height:300,

            margin:0,

            navText: [

                '<i class="fa fa-angle-left"></i>',

                '<i class="fa fa-angle-right"></i>'

            ],

            autoplay: true,

            autoplayTimeout: 3000,

            autoplayHoverPause: true,

            responsive: {

                0:{

                    items:1

                },

                480:{

                    items:1

                },

                600:{

                    items:1

                },

                768:{

                    items:2

                },

                1000:{

                    items:2

                },

                1200:{

                    items:3

                },

                1920:{

                    items:3

                },

            }

        });

    }

}





// add your custom functions 

function testimonialsCarosule () {

    if ($('#testimonials .owl-carousel').length) {

        $('#testimonials .owl-carousel').owlCarousel({

            loop: true,

            margin: 30,

            nav: false,

            dots: true,

            autoplay: false,

            navText: [

                '<i class="fa fa-angle-left"></i>',

                '<i class="fa fa-angle-right"></i>'

            ],

            autoplayHoverPause: true,

            responsive: {

                0:{

                    items:1

                },

                480:{

                    items:1

                },

                600:{

                    items:1

                },

                768:{

                    items:2

                },

                1000:{

                    items:2

                },

                1200:{

                    items:3

                },

                1920:{

                    items:3

                }

            }

        });

    }

}



// add your custom functions 

function blogCarosule () {

    if ($('#blog .owl-carousel').length) {

        $('#blog .owl-carousel').owlCarousel({

            loop: true,

            nav: true,

            dots: false,

            height:300,

            margin:30,

            navText: [

                '<i class="fa fa-angle-left"></i>',

                '<i class="fa fa-angle-right"></i>'

            ],

            autoplay: true,

            autoplayTimeout: 3000,

            autoplayHoverPause: true,

            responsive: {

                0:{

                    items:1

                },

                480:{

                    items:1

                },

                600:{

                    items:1

                },

                1000:{

                    items:1

                },

                1200:{

                    items:1

                },

                1920:{

                    items:1

                },

            }

        });

    }

}





// add your custom functions 

function clientCarosule () {

    if ($('#clients .owl-carousel').length) {

        $('#clients .owl-carousel').owlCarousel({

            loop: true,

            nav: true,

            dots: false,

            margin:70,

            autoWidth: true,

            navText: [

                '<i class="fa fa-angle-left"></i>',

                '<i class="fa fa-angle-right"></i>'

            ],

            autoplay: true,

            autoplayTimeout: 3000,

            autoplayHoverPause: true,

            responsive: {

                0:{

                    items:1

                },

                480:{

                    items:2

                },

                600:{

                    items:3

                },

                1000:{

                    items:5

                },

                1200:{

                    items:5

                }

            }

        });

    }

}



// wow activator

function wowActivator () {

    var wow = new WOW ({

        offset: 0

    });

    wow.init();

}



// instance of fuction while Document ready event   

jQuery(document).on('ready', function() {

    (function($) {

        serviceCarosule();

        testimonialsCarosule()

        blogCarosule()

        clientCarosule();


        CounterNumberChanger();

        wowActivator();



    })(jQuery);

});



// instance of fuction while Window Load event

jQuery(window).on('load', function() {

    (function($) {



    })(jQuery);

});



// instance of fuction while Window Scroll event

jQuery(window).on('scroll', function() {

    (function($) {

		

    })(jQuery);

});

